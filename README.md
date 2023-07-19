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

*ESP32(comminicate between components and Internet)*

![esp32-esp-32s-wifi-bluetooth-dual-mode-developement-board-37182-73-B](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/485a1d5b-64e4-47ae-a275-bb5a1db75360)


**Solution Architecture**

![DEU-DT_Machine_SA_V2 drawio (1)](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/f53c1ec2-5d30-4efc-bbd9-4d4fe7cd46a4)

## Assembling The Arm
**Assembling the servo motors with chop-sticks**

![Assembled Servo Motors With Chop-Sticks](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/45431c07-27ae-4cf4-8fa2-6b7f00202826)

**Assembling the potentiometers with chop-sticks**

![potentioAssemble](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/d304b0ae-4658-4cd6-8e2d-4f762dd17807)

**Get together potetiometers, servo motors, and make connection with ESP32**

![servo_esp32_potentio_assemble](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/838c28cb-599a-43e7-b091-459ddcebac87)

**Cable Connections**

(circuit diagram foto)


Now Add Pyhton Codes to ESP32


**Sending Data to NODE-RED Using MQTT Protocol Using DOCKER**

**Creating DataBase and Sending Data**

**Visualise Data**
