from umqtt.simple import *
from time import sleep

class Pub:
    def __init__(self,clientName, serverAdd):
        self.client = clientName
        self.serverAdd = serverAdd
        self.mqttc = MQTTClient(client_id=clientName,server=serverAdd, port=1883,keepalive=60)

    def publish(self,topic,msg):
        self.mqttc.publish(topic.encode(), str(msg).encode())
    
    def disconnect(self):
        self.mqttc.disconnect()
    
    def connect(self):
        self.mqttc.connect()

class Rec:
    def __init__(self,clientName, serverAdd, topic):
        self.client = clientName
        self.serverAdd = serverAdd
        self.topic = topic
        self.mqttc = MQTTClient(client_id=clientName,server=serverAdd, port=1883,keepalive=60)
        self.val = 0
        
    def sub_cb(self,topic ,msg):
        msg = (msg.decode().split(',')[0]).replace('[','').replace(']','')
        self.val = int(msg)

    def returnVal(self):
        return self.val
    
    def receive(self):     
        self.mqttc.check_msg()

    def disconnect(self):
        self.mqttc.disconnect()
    
    def connect(self):
        self.mqttc.connect()  
        self.mqttc.set_callback(self.sub_cb)
        self.mqttc.subscribe(self.topic.encode())        


