# Project-Sunfish
Summer internship project funded by the University of Idaho

**Project Authors:** 
&nbsp;&nbsp;&nbsp;&nbsp;led by Ethan Carpenter, supported by Isaiah Preston and Karson Vordahl 

**Project Supervisors**
&nbsp;&nbsp;&nbsp;&nbsp;Dr. John Shovic and Dr. Marz Everett 

# Overview

&nbsp;&nbsp;&nbsp;&nbsp;Project sunfish is designed to eliminate costly manual sampling of lake Coeur D' Alene. The current process requires a boat trip to the verified satellite locations where there are indicators of harmful algal bloom and heavy metal contents, and the completion of the manual sampling process, which entails collecting each sample individually, at 3 separate depths. Once collected, these samples are then safely, and without contaminating, dumped into a sampling container and then put into a cooler. These samples then are only considered "fresh" for a certain ammount of time before they are not useful for testing. The limitations introduced by this process are the costs and availability of the boat, as well as personnel to operate the boat and take the samples, this operation also has a limited window of time where this can successfully be completed, you cannot take the boat out in the winter time therefore you can not sample the areas in that time, resulting in months of no data collected. 

&nbsp;&nbsp;&nbsp;&nbsp;Sunfish will solve many of these problems and more. Sunfish is a commercially available drone produced by BlueRobotics, and assembled in 2019 by a previous graduate student. It has since been converted to serve this purpose, by designing and retrofitting an automated collection device, for taking samples, as well as adding relevant equipment to create a cohesive device. 

# Phases

There is three main phases to this project

**Phase one:**
&nbsp;&nbsp;&nbsp;&nbsp;Restoring Sunfish back to "factory" configuration and hardware to ensure working components and testing

**Phase two:**
&nbsp;&nbsp;&nbsp;&nbsp;Developing automated collection device and testing

**Phase three:**
&nbsp;&nbsp;&nbsp;&nbsp;Testing components together and collecting samples with sunfish

# Phase One

&nbsp;&nbsp;&nbsp;&nbsp;After retrieving Sunfish from storage, the first task was opening up both enclosures and cleaning all of the components. After sitting in storage for 4-5 years, Sunfish needed a tune-up.

<img width="5712" height="4284" alt="IMG_9633" src="https://github.com/user-attachments/assets/bae438af-0f04-41d9-b9de-6e320f62e1a2" />
First look at sunfish once pulled from storage



&nbsp;&nbsp;&nbsp;&nbsp;This was done by removing all of the electronics from the enclosures and unseating all of the connections. This was done over the course of 2 days, cleaning and identifying and labeling what each of the components do and where they are located. This allowed me to see what we had and what was unneeded for the project and what components couldn't be sacrificed. 


<img width="3024" height="4032" alt="IMG_9712" src="https://github.com/user-attachments/assets/d98c8b99-f567-4899-ad99-9453a0c3b29b" />
<img width="3024" height="4032" alt="IMG_9712" src="https://github.com/user-attachments/assets/40035f61-f466-46ae-8fb8-4990fa66b178" />
Electronics, and how they were seated in the main enclosure 


<img width="4284" height="5712" alt="IMG_9715" src="https://github.com/user-attachments/assets/848552d6-701e-44df-9449-8dc53b736995" />
Sunfish with all of the enclosures removed and the electronics off the frame


<img width="3024" height="4032" alt="IMG_9722" src="https://github.com/user-attachments/assets/fc15c4b3-5d5b-48b6-85ba-0645b7a05a62" />
Electronics cluster after putting everything back together the first time




&nbsp;&nbsp;&nbsp;&nbsp;After the completion of our first successful dive, we identified some small issues and somethings that needed to be fixed. There was a small leak in the main enclosure, during the dive the enclosure took on about 2 tablespoons of water, and one of the main steering thrusters on the front side was non-operational. After further inspection of the non-operational thruster, it appeared that while in storage, there was stagnant water inside the thruster itself on the brushless motor and corroded part of the thrusters battery housing, which caused the motor to then grind on itself and cause damage to the thruster itself. The solution was simple, the non-operational thruster was then moved from the primary steering position, to one of the "extra" slots alvailabe on the top side, used for surfacing the drone, this slot was available and did not affect any operation of the drone due to this being part of the optional "heavy thruster configuration" that was purchased, which added an extra 2 thrusters to the surfacing (or top side) portion of the drone. Once swapped the next challenge was identifying and fixing the leak.

&nbsp;&nbsp;&nbsp;&nbsp;Each enclosure housing has three separate parts to it, 2 end caps, which split open to 2 different parts each, and the acrylic tube itself. So, taking apart each component of the housings, each o-ring was replaced and a fresh coat of silicon waterproofing grease was applied. After putting the enclosure back together a pressure test was conducted.(See "Conducting a Pressure Test") Once reached 15mm/hg, it needs to sit for 10 minutes, if the pressure drops below 14mm/hg in that 10 minutes the pressure test is considered a failure and is not safe to put in the water. The sub continually failed these pressure tests, it was pointed out that it might be the enclosure itself, so we swapped the factory 12" acrylic enclosure tube with a 18" acrylic enclosure, nicknamed "Extendo-Tubo". Once replacing the tube, the leak slowed, but it was still failing the pressure tests. To be through, before ordering all new components,  I removed each of the plugs on the back of the enclosure, these seating screws have the wires leading to each of the thrusters as well as the lights and the battery enclosure, protruding from the back, in order to unseat these screws, you have to remove the thrusters from their mounted position. After removing the enclosure bolts, you will see a small o-ring on the inside face of the bolt, all 18 of the o-rings were pulled, replaced and re-greased. They were then screwed back in and torqued by hand to the correct positions. The same was done for the smaller cap screws that are used to hold the 2 different parts of the end caps together. After replacing and torquing them down with a Allen key by hand, Another pressure test was conducted, this test passed and we were ready for our second successful dive (see "Prepping For a Dive").

# Conducting a Pressure Test

&nbsp;&nbsp;&nbsp;&nbsp;In order to conduct a proper vacuum test, you will need the provided vacuum pump. 
- Ensure both the brass male pieces have intact o-rings, and there is no debris on them.
- Seat each male end inside the female ends on the rear of the sub, one on the rear of the main enclosure and the other on the rear of the &nbsp;&nbsp;&nbsp;&nbsp;battery enclosure, the female ends are labeled "Vent"
- Depress the handle of the vacuum pump, effectively removing the air from both enclosures
- To achieve a 15mm/hg readout on the face of the pump, it will take about 300 depressions.
- Once the needle is reading 15mm/hg set a timer for 10 minutes and place the pump somewhere upright and secure (if the pump is not upright, it has been noticed that it will affect the interior pressure for some reason, my guess is that it causes the tube to twist, therefore adding pressure into the enclosure)
- After the 10 minutes is up, if the reading is between 15mm/hg and 14mm/hg, it has passed and you are safe to dive, if the reading is below the 14mm/hg line, it has failed, the first step should be to remove the caps from the enclosures and inspect for debris along the o-rings and repeat the steps above.


# Prepping For a Dive

&nbsp;&nbsp;&nbsp;&nbsp;Congradulations! if you are reading this, you have passed the pressure tests and you are ready to dive.


&nbsp;&nbsp;&nbsp;&nbsp;You will need the following items:
- QGroundControl software installed on your computer, if you're using your personal computer for the dive, or one of the two computers that come with the project has the software already installed. 
- Sunfish itself
- 300 meter tether (this is the spooled tether)
- smaller tether (This tether is wrapped up in the backpack and is used to attach to the spool, and then to the fathomX interface box)
- Fathom X interface box (blue box with a power cord found with it)
- Fathom X interface box power cord
- USB cable that attaches the Fathom X box to your computer
- Xbox controller (wired or wireless)
- Costco wagon (so you can load everything into the wagon and transport to the launch site)
- Sunfish backpack (in this backpack, you will store everything but the sunfish and the 300m tether, inside the backpack is a flat tackle box tray that holds extra components that you might need as well as a wrench that fits the enclosure cap screws. I suggest throwing in a IFIXIT setup so you can easily remove the smaller cap screws)

&nbsp;&nbsp;&nbsp;&nbsp;Before loading everything up in the wagon and making the trek to the launch site, you need to do a couple of things first.

- You will need to ensure that there is no leak in the enclosure, always perform a pressure test before you go out for a dive, even if you tested the day before and it passed, something might have changed overnight that is unseen, always do a pressure right before you leave for launch, or if the sub experiences a lot of jostling around during transport, you will need to perform one at the launch site.
- Boot up QGroundControl and run through the diagnostics, this is done by following these steps which are provided on the BlueRobotics web page
  &nbsp;&nbsp;&nbsp;&nbsp;https://bluerobotics.com/learn/bluerov2-software-setup/#installing-qgroundcontrol
  















