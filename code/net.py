import network

class Net:
    def __init__(self,ssid, psw):
        self.station = network.WLAN(network.STA_IF)
        self.ssid = ssid
        self.psw = psw
    
    def connect(self):
        if self.station.isconnected() == True:   
            print("Already connected")
            return

        self.station.active(True) 

        self.station.connect(self.ssid, self.psw)
        while self.station.isconnected() == False:
            pass

        print("Connection successful")  
        print(self.station.ifconfig())

    def disconnect(self):
        if self.station.active() == True: 
            self.station.active(False)
        if self.station.isconnected() == False:  
            print("Disconnected")

