![image](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/08c2d3b5-a7d2-4914-b3f2-d501c46553a0)

# Robot Arm Tutorial

Digital Twin in Machinery and Tools – Miniature Robot Arm with Potentiometer-based Control and MQTT Communication
> **Demonstration video is located at the bottom of this document.**

## BRD (Business Requirements)

Executive Summary

Firstly, the robotic arm is going to be assembled. Movement of the robotic arm will be handled with
potentiometers. Potentiometers movement position save and repeatedly making the move after pressing button.
Fetching and displaying data will be handled.

Objectives

- Construct a functional miniature robot arm using 3D model as the primary building material.
- Integrate four potentiometers to enable precise control of the robot arm's movements.
- Implement an MQTT communication in microPython to facilitate data exchange between the
robot arm and external devices.
- Sending datas to a Database

Project Scope

Minimizing human requirements and errors in the industrial arms with remote control capabilities and
watching the industrial arm's conditions in real time.

## Components

*1 Servo for clipper (open-close)*

*4 MG996R Servo (controlling each arm link)*

*4 10K Potentiometer(to move MG996R servos with potentiometers)*

*4 Button(for mutiple feature)*
- 1 for switching server and potentiometer controlling
- 1 for record arm movements
- 1 for playing this record
- 1 for open and close clipper to hold objects

*ESP32(comminicate between components and Internet)*

## Assembling The Arm
**Assembling the servo motors, potentiometers and making cable connections circuit desing**

![ESP32CircuitDiagramV5](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/23ebbd96-525e-4696-9a99-da37cd3d2bbf)

**Get together potetiometers, servo motor, and make connection with ESP32**

![robotArm2](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/6be566cc-aa5a-4c35-b995-0484e72c797d)

**Now Add Pyhton Codes to ESP32**

## Node-Red and Internet Part

**Creating Node-Red Flow**
MQTT_in nodes connects a topic and gets sends data to gauges
MQTT_out nodes send data to ESP32  from sliders
Orange nodes helps to store data to SQLite database

![node-redFlow](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/aac00e82-0267-46b0-9602-24e12cf8e93d)
*Main Robot Arm*

![node-redFlowScara](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/76052f0e-2ddb-4db0-8cb8-28b0da98633b)
*SCARA Arm*

**Creating Node-Red UI**
Sliders helps to control servos in Node-Red
Gauges are shows the angle of potentiometers and servos
Database is a SQLite database that stores the servo names, values, and status

![node-redUI](https://github.com/berkayguzel06/Robot-Arm/assets/98205992/a1f10409-3f53-42a6-8686-6eeeba0e6468)

## Robot Arm Demo Video

Watch the demonstration video

https://github.com/berkayguzel06/Robot-Arm/assets/98205992/1ceb1cf3-8ca9-4a95-af73-3f9df5756e0d

This project aims to provide precise control and remote monitoring capabilities for industrial arms, ultimately reducing human intervention and minimizing errors. It demonstrates the integration of hardware, software, and data handling to create a functional miniature robot arm.
