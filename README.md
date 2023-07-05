# Robot Arm Tutorial

Digital Twin in Machinery and Tools – Miniature Robot Arm with Potentiometer-based Control and MQTT Communication

__BRD (Business Requirements)__

Executive Summary

Firstly, the robotic arm is going to be assembled. Movement of the robotic arm will be handled with
potentiometers. Potentiometers movement position save and repeatedly making the move after pressing button.
Fetching and displaying data will be handled. Creating a model and simulating with
Unity. Lastly, applying machine learning.

Objectives

-Construct a functional miniature robot arm using pop-sticks as the primary building material.
- Integrate four potentiometers to enable precise control of the robot arm's movements.
- Implement an MQTT communication system in microPython to facilitate data exchange between the
robot arm and external devices.
- Learn the basics of Unity / ABB RobotStudio
- Create a model on Unity / ABB RobotStudio
- Simulate the Digital Twin created on Unity / ABB RobotStudio using the MQTT communication
- Apply Machine Learning to predict RUL (remaining useful life)

Project Scope

Minimizing human requirements and errors in the industrial arms with remote control capabilities and
watching the industrial arm's conditions in real time.

__Components__

Pop-Sticks(for fasten the potentiometers, cables, servos) 
Cables

*4 Servo(for moving arm)*

![tower-pro-sg90-rc-mini-servo-motor-27734-15-O](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/6089d2a8-8e00-4b01-b1b5-287d6eba752e)

*4 Potentiometer(to move arms with potentiometers)*

![1K Potentiometer Tone Control](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/818d1beb-f3f1-49c4-90d1-45147cfbbf8a)

*1 Button(for changing movement mode)*

![51v2BfPNn+L _AC_SR263,263_QL70_](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/f62af6e7-0942-405d-8be6-b0a72fb310ad)

*ESP32(comminicate between components and commend move)*

![ESP32-ESP32S-ESP-32S-ESP-32-CP2102-kablosuz-WiFi-Bluetooth-geli-tirme-kurulu-mikro-USB-ift](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/67400aff-2aeb-4189-a466-e98cba80383d)


__Solution Architecture__

![image](https://github.com/berkayguzel06/Robotic_Arm/assets/98205992/6f2dd60f-a43e-4943-bf03-877cee7a59eb)

__REFERENCES__

https://randomnerdtutorials.com/getting-started-with-esp32/
https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/
https://www.upesy.com/blogs/tutorials/esp32-servo-motor-sg90-on-micropython




