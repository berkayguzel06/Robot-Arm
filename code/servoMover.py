from servo import Servo # servo.py
from machine import Pin

class Servos:
    def __init__(self) -> None:
        self.motors = []
        self.servoPins = []
    # Attaches the servos to the ESP32
    def attach(self, pinNum):
        if pinNum not in self.servoPins:
            self.servoPins.append(pinNum)
            self.motors.append(Servo(pin=Pin(pinNum)))
        else:
            print("Pin is occupied")
    # Move the servos with mapped value
    def move(self, vals):
        for i in range(4):
            val = vals[i]
            mapped_val = _map_range(val, 0,2047 ,0 ,180)
            self.motors[i].write_angle(degrees=mapped_val)
            
# Map function
def _map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

