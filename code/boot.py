# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
# Connects the ESP32 to internet
print("Boot: RUN")
from net import Net

w = Net('ssid', 'password')
w.connect()