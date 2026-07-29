#! /usr/bin/env python
import numpy as np
import rospy
from dynamixel_sdk import *
import os
import time
import sys
import ctypes

open = [484, 558]
close = [710, 310]

#Notes:
#I think to get this to protocol 2 the major change is just the packetHandler. This is something to look into. 

#This info is for our SPECIFIC gripper (not necessarily generalizable)
ids = [1, 2]
limits = [[484, 729], [320, 558]]
#ct stands for control table
AX_ct_names = ["Model_Number", "Firmware_Version", "ID", "Baud_Rate", "Return_Delay_Time", "CW_Angle_Limit",
                           "CCW_Angle_Limit", "Temperature_Limit", "Min_Voltage_Limit", "Max_Voltage_Limit", 
                           "Max_Torque", "Status_Return_Level", "Alarm_LED", "Shutdown", "Torque_Enable",
                           "LED", "CW_Compliance_Margin", "CCW_Compliance_Margin", "CW_Compliance_Slope",
                           "CCW_Compliance_Slope", "Goal_Position", "Moving_Speed", "Torque_Limit",
                           "Present_Position", "Present_Speed", "Present_Load", "Present_Voltage", "Present Temperature",
                           "Registered", "Moving", "Lock", "Punch"]
AX_ct_addr = [0, 2, 3, 4, 5, 6, 8, 11, 12, 13, 14, 16, 17, 18, 24, 25, 26, 27, 28, 29, 30, 32, 34, 
                              36, 38, 40, 42, 43, 44, 46, 47, 48]
AX_ct_len = [2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2]


#This class assumes you are using a chain of the EXACT same type of motors. It cannot handle multiple motor types in one chain at this time. 
class dynamixelMotorControl:
   def __init__(self, type, baudrate, portName, protocol, speed = 100, list_of_ids=ids, list_of_limits=limits, threshold=10):
      #Type initialization
      self.type = type
      if type == "AX-18A" or type == "AX-18F":
         #Assign the motor specific lists
         self.ct_names = AX_ct_names
         self.ct_addr = AX_ct_addr
         self.ct_len = AX_ct_len
         self.speed = 100
      else:
         print("ERROR: Unknown Motor Type. Unable to initialize motor.")
         return 
      
      #Motor specific values setup
      self.ids = ids
      self.limits = limits
      self.torque_enable_addr = AX_ct_addr[AX_ct_names.index("Torque_Enable")] 
      self.goal_position_addr = AX_ct_addr[AX_ct_names.index("Goal_Position")]
      self.present_position_addr = AX_ct_addr[AX_ct_names.index("Present_Position")]
      self.goal_position_len = AX_ct_len[AX_ct_names.index("Goal_Position")]
      self.present_position_len = AX_ct_len[AX_ct_names.index("Present_Position")]
      
      #communication setup
      self.baudrate = baudrate
      self.portName = portName
      self.protocol = protocol

      #From SDK
      self.portHandler = PortHandler(self.portName)
      self.packetHandler = PacketHandler(self.protocol)
      
      #These lists will keep track of the writer objects we decided to use for the dynamixels
      self.writer_names = []
      self.writer_objects = []
      #Bulk Reader Object, for Protocol 1
      self.groupBulkRead = GroupBulkRead(self.portHandler, self.packetHandler)

      #Misc
      self.moving_threshold = threshold
      self.torque_enable = 1
      self.torque_disable = 0

   #Take find the address at the specified control table name 
   def getAddress(self, ct_name):
      return self.ct_addr[self.ct_names.index(ct_name)]

   #Find the bytelength at the specified control table name
   def getLength(self, ct_name):
      return self.ct_len[self.ct_names.index(ct_name)]

   #Begin the motor. Setup and open the port, read in the motor limits, set the initial motor speeds
   def begin(self):
      #This is also from the SDK
      print()
      # Open port
      if self.portHandler.openPort():
         print("Succeeded to open the port")
      else:
         print("Failed to open the port")        
         #quit()
      #Set the port's baudrate
      if self.portHandler.setBaudRate(self.baudrate):
         print("Baudrate Set.")
      else:
         print("Failed to Set Baudrate")
         #quit()
         return
      
      #Write the inital speed to the dynamixels
      for i in range(0, len(self.ids)):
         self.motorWrite(self.ids[i], "Moving_Speed", self.speed)
      
      #Write the motor limits to the dynamixel 
      for i in range(0, len(self.ids)):
         self.motorWrite(self.ids[i], "CW_Angle_Limit", self.limits[i][0])
         self.motorWrite(self.ids[i], "CCW_Angle_Limit", self.limits[i][1])
      
      #Enable the torque on all of the dynamixel motors in our chain. 
      for i in range(0, len(self.ids)):
         self.motorWrite(self.ids[i], "Torque_Enable", self.torque_enable)
      print()
      print("Motor is Ready to Begin")

   #Cutoff access to the motor -- Disable the motor's torque and close the comm port
   def end(self):
      for i in range(0, len(self.ids)):
         self.motorWrite(self.ids[i], "Torque_Enable", self.torque_disable)
      self.portHandler.closePort()
      print("Motor Access Off")
  
  #Ping the motors by spedified ID, get back the model number
   def ping(self, Ids):
      for i in range(0, len(Ids)):
         dxl_model_number, dxl_comm_result, dxl_error = self.packetHandler.ping(self.portHandler, Ids[i])
         if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
         elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
         else:
            print("[ID:%03d] ping Succeeded. Dynamixel model number : %d" % (Ids[i], dxl_model_number))

   #Read 1 thing from a dynamixel motor (not synced)
   def motorRead(self, id, name):
         size = self.getLength(name)
         addr = self.getAddress(name)
         if size == 1:
            data, dxl_comm_result, dxl_error = self.packetHandler.read1ByteTxRx(self.portHandler, id, addr)
         elif size == 2:
            data, dxl_comm_result, dxl_error = self.packetHandler.read2ByteTxRx(self.portHandler, id, addr)
         elif size == 4:
            data, dxl_comm_result, dxl_error = self.packetHandler.read4ByteTxRx(self.portHandler, id, addr)
         
         if dxl_comm_result != COMM_SUCCESS:
               print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
         elif dxl_error != 0:
               print("%s" % self.packetHandler.getRxPacketError(dxl_error))
         return data

   #This doesn't work in for AX models in Protocol 1.0. 
   #Synchronized Read of Several Values
   def motorSyncRead(self, Ids, name):
      addr = self.getAddress(name)
      length = self.getLength(name)
      print(addr)
      print(length)
      
      #Add the parameters for the bulk read
      for i in range(0, len(Ids)):
         dxl_add_result = self.groupBulkRead.addParam(Ids[i], addr, length)
         if dxl_add_result != True:
               print("[ID:%03d] groupBulkRead addparam failed" % Ids[i])
               return
         else:
            print("Added the parameter successfully")
      #time.sleep(1)
      #Do the bulk read
    
      dxl_result = self.groupBulkRead.txRxPacket()
      if dxl_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_result))
           
      #Actually get and print the data
      toReturn = []
      for i in range(0, len(Ids)):
         get_data_result = self.groupBulkRead.isAvailable(Ids[i], addr, length)
         if get_data_result != True:
            print("[ID:%03d] groupBulkRead getdata failed" % Ids[i])
         else:
            val = self.groupBulkRead.getData(Ids[i], addr, length)
            toReturn.append(val)
            print("Value of ", name, "For Motor", Ids[i], "is ", val)
      self.groupBulkRead.clearParam()
      return toReturn
      

   #Write 1 Thing to a Dynamixel Motor (not synced)
   def motorWrite(self, id, name, value):
      size = self.getLength(name)
      addr = self.getAddress(name)
      if size == 1:
         dxl_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, id, addr, value)
      elif size == 2:
         dxl_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, id, addr, value)
      elif size == 4:
         dxl_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, id, addr, value)
      
      #Handle Any Errors
      if dxl_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_result))
      elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
      else:
            print("Successfully wrote", value, "of ", name, " to Dynamixel#%d " % id)
 

   #Sync Write to the dynamixel motor. Multiple values stored in. 
   def motorSyncWrite(self, Ids, values, byteSize, writerObject):
      #Get the values into the correct format and add them to our paramters
      for i in range(0, len(Ids)):
         # Allocate goal position value into byte array -- GO BACK AND CHANGE THIS TO BE MORE FLEXIBLE, EVENTUALLY.
         if (byteSize == 2):
            #You need to investigate this. It's weird. 
            position = [DXL_LOBYTE(DXL_LOWORD(values[i])), DXL_HIBYTE(DXL_LOWORD(values[i]))]
         else:
            position = [DXL_LOBYTE(DXL_LOWORD(values[i])), DXL_HIBYTE(DXL_LOWORD(values[i])), DXL_LOBYTE(DXL_LOWORD(values[i])), DXL_HIBYTE(DXL_LOWORD(values[i]))]  
         #Add the parameters
         dxl_result = writerObject.addParam(Ids[i], position)
         if dxl_result != True:
            print("[ID:%03d] groupSyncWrite addparam failed" % Ids[i])
     
      #Actually Write the Values
      dxl_result = writerObject.txPacket()
      if dxl_result != COMM_SUCCESS:
         print("%s" % self.packetHandler.getTxRxResult(dxl_result))
      # Clear syncwrite parameter storage
      else:
         print("Successfully wrote", values, "to ", Ids)
      writerObject.clearParam()

  #Function to use when doing a synchronized write
   def syncWrite(self, Ids, name, values, wait=True, printStatus=True):
      addr = self.getAddress(name)
      length = self.getLength(name)
      threshold = 10
      if name in self.writer_names:
         writer = self.writer_objects[self.writer_names.index(name)]
      else:
         #Make a new writer object:
         print("Creating a new writer object")
         newObj = GroupSyncWrite(self.portHandler, self.packetHandler, addr, length)
         self.writer_objects.append(newObj)
         self.writer_names.append(name)
         writer = newObj
      self.motorSyncWrite(Ids, values, length, writer)
      if (wait == True):
         cont = 0
         while cont < len(Ids):
            #continue variable
            cont = 0
            newValues = []
            if name == "Goal_Position": #Special case specfific to movement
               #Read the Moving Status
               for i in range(0, len(Ids)):
                  newValues.append(self.motorRead(Ids[i], "Moving"))
                  #If the arm isn't moving, we can continue
                  if newValues[i] == 0:
                      cont += 1
            #Otherwise we'll use a threshold value to determine when to return from this function
            else: 
               for i in range(0, len(Ids)):
                  newValues.append(self.motorRead(Ids[i], name))
                  if (abs(values[i]) - newValues[i]) < self.moving_threshold:
                     cont += 1
            #We can print current position, goal position, speed, load, and voltage 
            if printStatus == True:
               self.printStatus(Ids)

   #Print Info about the init's you made for the motor
   def printInfo(self):
      print()
      print("Motor Type: ", self.type)
      print("Communication:")
      print("Baudrate:", self.baudrate)
      print("PortName:", self.portName)
      print("Protocol:", self.protocol)
      print("Motor Specific Info: ")
      print("Motor ID's", self.ids)
      print("Motor Min and Max Limits", self.limits)
      print("Moving Threshold", self.moving_threshold)
      print()

   #Read in and Print current position, goal position, speed, load, voltage
   def printStatus(self, Ids):
      current_positions = []
      goal_positions = []
      current_speed = []
      current_load = []
      current_voltage = []
      for i in range(0, len(Ids)):
         current_positions.append(self.motorRead(Ids[i], "Present_Position"))
         goal_positions.append(self.motorRead(Ids[i], "Goal_Position"))
         current_speed.append(self.motorRead(Ids[i], "Present_Speed"))
         current_load.append(self.motorRead(Ids[i], "Present_Load"))
         current_voltage.append(self.motorRead(Ids[i], "Present_Voltage"))
      print("------------------------Status-----------------------------")
      print("Current Positions", current_positions)
      print("Goal Positions", goal_positions)
      print("Current Speed", current_speed)
      print("Current Load", current_load)
      print("Current Voltage", current_voltage)
      print("-----------------------------------------------------------")
   


#Main Program 
def main():
   init_speed = 100
   gripper = dynamixelMotorControl("AX-18F", 1000000, '/dev/ttyUSB0', 1.0)
   gripper.printInfo()
   gripper.begin()
   #waveHi(gripper)
   #openShut(gripper)
   gripper.ping([1, 2])

   gripper.end()

if __name__=="__main__":
    main()
