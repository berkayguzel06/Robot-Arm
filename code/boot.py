# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
print("Boot: RUN")
from net import Net

w = Net('name', 'password')
w.connect()