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

<img width="600" height="450" alt="IMG_9633" src="https://github.com/user-attachments/assets/bae438af-0f04-41d9-b9de-6e320f62e1a2" />

First look at sunfish once pulled from storage



&nbsp;&nbsp;&nbsp;&nbsp;This was done by removing all of the electronics from the enclosures and unseating all of the connections. This was done over the course of 2 days, cleaning and identifying and labeling what each of the components do and where they are located. This allowed me to see what we had and what was unneeded for the project and what components couldn't be sacrificed. 


<img width="600" height="450" alt="IMG_9712" src="https://github.com/user-attachments/assets/d98c8b99-f567-4899-ad99-9453a0c3b29b" />
<img width="600" height="450" alt="IMG_9712" src="https://github.com/user-attachments/assets/40035f61-f466-46ae-8fb8-4990fa66b178" />

Electronics, and how they were seated in the main enclosure 


<img width="600" height="450" alt="IMG_9715" src="https://github.com/user-attachments/assets/848552d6-701e-44df-9449-8dc53b736995" />

Sunfish with all of the enclosures removed and the electronics off the frame


<img width="600" height="450" alt="IMG_9722" src="https://github.com/user-attachments/assets/fc15c4b3-5d5b-48b6-85ba-0645b7a05a62" />

Electronics cluster after putting everything back together the first time




&nbsp;&nbsp;&nbsp;&nbsp;After the completion of our first successful dive, we identified some small issues and somethings that needed to be fixed. There was a small leak in the main enclosure, during the dive the enclosure took on about 2 tablespoons of water, and one of the main steering thrusters on the front side was non-operational. After further inspection of the non-operational thruster, it appeared that while in storage, there was stagnant water inside the thruster itself on the brushless motor and corroded part of the thrusters battery housing, which caused the motor to then grind on itself and cause damage to the thruster itself. The solution was simple, the non-operational thruster was then moved from the primary steering position, to one of the "extra" slots available on the top side, used for surfacing the drone, this slot was available and did not affect any operation of the drone due to this being part of the optional "heavy thruster configuration" that was purchased, which added an extra 2 thrusters to the surfacing (or top side) portion of the drone. Once swapped the next challenge was identifying and fixing the leak.

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
- Battery for the sub (this should be charged before the dive fully so it does not die in the water)
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
- Once you have completed the Sensor Calibration you need to ensure that in the "Vehicle Setup" tab, under "Frame" you need to ensure the BloueROV2 Heavy/Vectored 6DOF setting is enabled. Remember, that after each calibration setting that is changed, you have to reboot the vehicle entirely.
- After successful completion of these steps, the previously yellow bar on the top left of the screen, will turn green and say "Ready to Launch"
- You then are ready for your launch and are ok to load everything up and head to your launch site

&nbsp;&nbsp;&nbsp;&nbsp;**Launching** 

- When at your launch point, remove everything from the wagon and set up your area
- Make sure you have QGroundControl launched on your computer and the Fathom X Topside Interface plugged into your computer
- On the back of sunfish there is a male plug, plug the matching female end from the spooled tether into that and secure it multiple times with electrical tape to ensure it is fully waterproofed.
- Then connect the looped end of the tether, to the carabiner clip attached to the sub. This makes it so if you need to retrieve it for any reason, you can pull on the tether to reel it back in and not put tension on the plug itself. This is what the tether is made for.
- Hook the smaller tether to the spool side and then to the Fathom X Topside Interface
- Plug in the Xbox controller to your computer.
- You can either choose to place the sunfish in the water gently, or toss it in from the dock if you are on a dock, if you are just on the embankment of a river or the lake, do not throw it, place the drone in the water, so it is all covered, you are going to want to have enough submersion so it can have plenty of room to move up and forward so it doesn't scrape on the bottom.
- It is also a wise idea to have someone in the water with sunfish, two people are preferred if you are launching off a dock, and one person suffices if you are launching in a shallower area.
- Once the sub is fully submerged, click the green "Ready to Launch" button. a small slider arrow will pop up on the bottom of the screen the reads "ready to arm" slide this to the right and the sunfish will arm and then be operational.

&nbsp;&nbsp;&nbsp;&nbsp;Congratulations on your successful dive!

# Automatic Sample Collection Device

&nbsp;&nbsp;&nbsp;&nbsp;The current prototype is what I am calling a "dry prototype" this means its not waterproofed, or ready for diving, only a concept of what this will look like and how it can function, without tackling any of the waterproofing factors. The design consists of a 3D printed honeycomb enclosure that encases a bag with a silicon tube. There is also a "lid" that vertically slides into place over the mouth, that has a channel you can feed the tube through, the tube will end up facing vertically out of the channel, in line with the cover. Inside the tube is placed a ball check valve that has been 3D printed and designed by Ethan Carpenter, this consists of, 3 parts, the "stem", which is a short pipe, which graduates into a wider pipe with a little shelf in the middle for the spring to sit on. the "spring and ball" which is exactly what it sounds like, a spring attached to a ball. Finally the "Cover" this cover has an o-ring attached to it and gets superglued over the spring and ball, creating a seal. 

&nbsp;&nbsp;&nbsp;&nbsp;The plan is to have a Dynamixal servo motor (either the AX-18a or the AX-12a) push down on the ball, releasing the pressure and causing the bag to fill with water. when the sample is completed, it will then release the downward pressure it is holding on the ball and then cause the water flow to be cutoff. This design has been tested without the Dynamixal, and has shown one issue that I have seen. The main issue is that the bag, being deflated and no air inside, so to not affect the buoyancy of the sub, needs some sort of external force placed upon the bag encourage it to open. This is how we avoid using an actual pump at the end to pump the water in. I have thought of attaching somehow a spring to both sidewalls of the bags and then to the outer honeycomb enclosure, that would, when the ball valve is open, force the bag to open, therefore sucking water in and filling it. but I don't think that there is enough force applied by the spring to suck that much water in, this could be because the tube itself is at a 90degree angle, so there is limited room for the water to come in, as well as not enough pressure to pull water inside. The second idea I had, was having a compressed spring inside the bag, it would need to be powerful, and sterile so it docent affect the sample, but if it were compressed inside the bag, and then once the tube is open, it expands, that might create enough force to pull water in, of course then you would have a spring in your sample and then need to get it out. One other idea I had was to create a new bag system that made it so the bag itself was filled with air, and being submerged, this added air might counteract the weight added by the collection device. This would also mean that we would need to add a vent hose out of the top of the bag, so when water comes in, the air isn't escaping through the same hole.

<img width="600" height="450" alt="IMG_0569" src="https://github.com/user-attachments/assets/069e03a5-2183-47bb-8c40-49547a425aa7" />

&nbsp;&nbsp;&nbsp;&nbsp;Ball check valve 3D printed Prototype 

<img width="600" height="450" alt="IMG_0571" src="https://github.com/user-attachments/assets/f3223b0f-f49e-4d14-8ed5-c1ef57d80b91" />
<img width="600" height="450" alt="IMG_0572" src="https://github.com/user-attachments/assets/9ff41bca-bf83-4f42-9dab-de8848500802" />

&nbsp;&nbsp;&nbsp;&nbsp;3D printed honeycomb enclosure

<img width="600" height="450" alt="IMG_0574" src="https://github.com/user-attachments/assets/6d89df80-d436-4595-a29e-9180a8ff3344" />
<img width="600" height="450" alt="IMG_0573" src="https://github.com/user-attachments/assets/c760dba5-bf34-4c0d-b70b-a1020fd685a6" />

&nbsp;&nbsp;&nbsp;&nbsp;Lid with sampling tube fed through









