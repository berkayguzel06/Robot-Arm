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
- Implement an MQTT communication in microPython to facilitate data exchange between the
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

## Assembling The Arm
**Assembling the servo motors, potentiometers and making cable connecitons circuit desing**

![ESP32CircuitDiagramV5](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/23ebbd96-525e-4696-9a99-da37cd3d2bbf)

**Get together potetiometers, servo motors, and make connection with ESP32**

![circuit_desing_foto](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/4d416748-c8c8-4df1-9d07-d59ac4d5a975)

**Now Add Pyhton Codes to ESP32**

## Node-Red and Internet Part

**Creating Node-Red Flow**
MQTT_in nodes connects a topic and gets sends data to gauges
MQTT_out nodes send data to ESP32  from sliders
Orange nodes helps to store data to SQLite database

![node-red_flow](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/11f972ff-0845-437c-a2c5-e6e862d8556a)

**Creating Node-Red UI**
Sliders helps to control servos in Node-Red
Gauges are shows the angle of potentiometers and servos
Database is a SQLite database that stores the servo names, values, and status

![node-red-ui](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/00515bc1-1e13-4fec-93df-a80d950748ed)
