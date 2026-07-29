#! /usr/bin/env python
import numpy as np


import dynamixel_controller as dmxl

open = [484, 558]
close = [710, 310]

#Gripper waves to you slowly
def waveHi(gripper):
   init_speed = 100
   wave1 = [484, 310]
   wave2 = [710, 558]

   while (init_speed < 150):
      gripper.syncWrite([1, 2], "Goal_Position", wave1)
      gripper.syncWrite([1, 2], "Goal_Position", wave2)
      init_speed += 10
      gripper.syncWrite([1, 2], "Moving_Speed", [init_speed, init_speed])

#Gripper opens and shuts, gets faster and faster
def openShut(gripper):
   init_speed = 100
   while (init_speed < 1000):
      gripper.syncWrite([1, 2], "Goal_Position", open)
      #time.sleep(5)
      gripper.syncWrite([1, 2], "Goal_Position", close)
      init_speed += 50
      gripper.syncWrite([1, 2], "Moving_Speed", [init_speed, init_speed])

#Main Program 
def main():
   init_speed = 100
   #Initialize motor model AX-18F with a baud rate of 1000000 on port USB0 using packet protocol 1.0
   gripper = dmxl.dynamixelMotorControl("AX-18F", 1000000, '/dev/ttyUSB0', 1.0)
   gripper.printInfo()
   gripper.begin()


   #waveHi(gripper)
   openShut(gripper)
   #gripper.ping([1, 2])

   gripper.end()

if __name__=="__main__":
    main()
