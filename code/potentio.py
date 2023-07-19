from machine import Pin, ADC
import time

class Pots:
    def __init__(self):
        self.pinNums = []
        self.pots = []
        self.atten = ADC.ATTN_11DB
        self.width = ADC.WIDTH_9BIT
    
    def attach(self,pinNum):
        if pinNum not in self.pinNums:
            pot = ADC(Pin(pinNum))
            self.pinNums.append(pinNum)
            pot.atten(self.atten) #potentio meter turn nearly 180 deg
            pot.width(self.width)
            self.pots.append(pot)
        else:
            print("Pin is occupied")    

    def read(self):
        return [x.read() for x in self.pots]

