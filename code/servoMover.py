from servo import Servo # servo.py
from machine import Pin

class Servos:
    def __init__(self) -> None:
        self.motors = []
        self.servoPins = []

    def attach(self, pinNum):
        if pinNum not in self.servoPins:
            self.servoPins.append(pinNum)
            self.motors.append(Servo(pin=Pin(pinNum)))
        else:
            print("Pin is occupied")

    def move(self, mapped_vals, prev_vals):
        for i in range(4):
            if abs(prev_vals[i] - mapped_vals[i]) > 4:
                self.motors[i].write_angle(degrees=mapped_vals[i])
                prev_vals[i] = mapped_vals[i]
            else:
                self.motors[i].write_us(0)