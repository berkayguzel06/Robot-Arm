# Robot Arm Tutorial

Digital Twin in Machinery and Tools – Miniature Robot Arm with Potentiometer-based Control and MQTT Communication

## BRD (Business Requirements)

Executive Summary

Firstly, the robotic arm is going to be assembled. Movement of the robotic arm will be handled with
potentiometers. Potentiometers movement position save and repeatedly making the move after pressing button.
Fetching and displaying data will be handled.

Objectives

-Construct a functional miniature robot arm using pop-sticks as the primary building material.
- Integrate four potentiometers to enable precise control of the robot arm's movements.
- Implement an MQTT communication using DOCKER system in microPython to facilitate data exchange between the
robot arm and external devices.
- Sending datas to a Database

Project Scope

Minimizing human requirements and errors in the industrial arms with remote control capabilities and
watching the industrial arm's conditions in real time.

## Components

Pop-Sticks(for fasten the potentiometers, cables, servos) 
Cables

*4 Servo(for moving arm)*

![towrpro_sg90](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/f4e308f1-529f-42a8-9e83-8806c4511df1)

*4 10K Potentiometer(to move arms with potentiometers)*

![10k-potans-potansiyometre-spike-55636-56-B](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/f572a792-8eae-4c5c-9ca6-14051aa3bcfb)

*1 Button(for changing movement mode)*

![09190-03-L-1](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/7ee6b8f5-09f8-4c25-98ab-92b3c878fd65)

*ESP32(comminicate between components and commend move)*

![esp32-esp-32s-wifi-bluetooth-dual-mode-developement-board-37182-73-B](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/485a1d5b-64e4-47ae-a275-bb5a1db75360)


**Solution Architecture**

![DEU-DT_Machine_SA_V2 drawio (1)](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/f53c1ec2-5d30-4efc-bbd9-4d4fe7cd46a4)

__REFERENCES__

https://randomnerdtutorials.com/getting-started-with-esp32/
https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/
https://www.upesy.com/blogs/tutorials/esp32-servo-motor-sg90-on-micropython




