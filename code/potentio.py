from machine import Pin, ADC
import time
'''
ADC.WIDTH_9BIT: range 0 to 511
ADC.WIDTH_10BIT: range 0 to 1023
ADC.WIDTH_11BIT: range 0 to 2047
ADC.WIDTH_12BIT: range 0 to 4095

ADC.ATTN_0DB — the full range voltage: 1.2V
ADC.ATTN_2_5DB — the full range voltage: 1.5V
ADC.ATTN_6DB — the full range voltage: 2.0V
ADC.ATTN_11DB — the full range voltage: 3.3V
'''
class Pots:
    def __init__(self):
        self.pinNums = []
        self.pots = []
        self.atten = ADC.ATTN_6DB
        self.width = ADC.WIDTH_11BIT
        self.EMA_S = []
        self.EMA_a = 0.2
    
    def attach(self,pinNum):
        if pinNum not in self.pinNums:
            pot = ADC(Pin(pinNum))
            self.pinNums.append(pinNum)
            pot.atten(self.atten) #potentio meter turn nearly 180 deg
            pot.width(self.width)
            self.pots.append(pot)
            self.EMA_S.append(pot.read())
        else:
            print("Pin is occupied")    

    def read(self):
        for i in range(len(self.pots)):
            self.EMA_S[i] = int((self.EMA_a * self.pots[i].read())+ ((1-self.EMA_a) * self.EMA_S[i]))
        return [x for x in self.EMA_S]

