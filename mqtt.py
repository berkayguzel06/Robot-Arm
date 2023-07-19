from umqtt.simple import *
from time import sleep

class Pub:
    def __init__(self,clientName, serverAdd):
        self.client = clientName
        self.serverAdd = serverAdd
        self.mqttc = MQTTClient(client_id=clientName,server=serverAdd, port=1883,keepalive=60)

        self.mqttc.connect()

    def publish(self,topic,msg):
        self.mqttc.publish(topic.encode(), str(msg).encode())

class Rec:
    def __init__(self,clientName, serverAdd, topic):
        self.client = clientName
        self.serverAdd = serverAdd
        self.mqttc = MQTTClient(client_id=clientName,server=serverAdd, port=1883,keepalive=60)
        self.val = 0
        
        def sub_cb(topic ,msg):
            msg = (msg.decode()).replace('[','').replace(']','')
            self.val = int(msg)
            

    
        self.mqttc.set_callback(sub_cb)
        self.mqttc.connect()
        self.mqttc.subscribe(topic.encode())

    def returnVal(self):
         return self.val
    
    def receive(self):      
            self.mqttc.check_msg()          


