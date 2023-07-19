from net import Net
from mqtt import Pub, Rec
from potentio import Pots
from time import sleep
import time
from machine import Pin
from servoMover import Servos

def start():
    prev = 0
    maxStep = 150
    count = 0
    recorded = []
    vals = [0,0,0,0]
    prevPotVals = [0,0,0,0]

    w = Net('SUPERONLINE_WiFi_7207', 'nyCkUhPDXzGJ')
    w.connect()

    p = Pub('Sender', 'mosquitto.baylav.org')
    baseR = Rec('baseReceiver', 'mosquitto.baylav.org','/staj/base')
    arm1R = Rec('arm1Receiver', 'mosquitto.baylav.org','/staj/arm1')
    arm2R = Rec('arm2Receiver', 'mosquitto.baylav.org','/staj/arm2')
    gripperR = Rec('gripperReceiver', 'mosquitto.baylav.org','/staj/gripper')

    # servos = Servos()
    # servos.attach(22) #base
    # servos.attach(23) #arm1
    # servos.attach(25) #arm2
    # servos.attach(26) #gripper

    pots = Pots()
    pots.attach(32) #base
    pots.attach(33) #arm1
    pots.attach(34) #arm2
    pots.attach(35) #gripper

    pauseBtn = Pin(18, Pin.IN)
    pauseFlg = False

    recordBtn = Pin(19, Pin.IN)
    recordFlg = False
    playBtn= Pin(21,Pin.IN)
    playFlg = False

    while True:      

        if recordBtn.value() == 1 and playFlg == False:
            recordFlg = True
        if playBtn.value() == 1 and recordFlg == False:
            playFlg = True
            
        if pauseBtn.value() == 1:
            pauseFlg = not pauseFlg

        if pauseFlg and not recordFlg:
            print("Recieving from Node-Red")
            baseR.receive()
            vals[0] = baseR.returnVal()
            arm1R.receive()
            vals[1] = arm1R.returnVal()
            arm2R.receive()
            vals[2] = arm2R.returnVal()
            gripperR.receive()
            vals[3] = gripperR.returnVal()
            print(vals)
            # servos.move(vals, prevPotVals)
            prevPotVals = vals
        elif not playFlg and not recordFlg:
            print("Sending from potentiometers")
            val = pots.read()
            print(val)
            # servos.move(val, prevPotVals)
            p.publish('/staj/base', val[0])
            p.publish('/staj/arm1', val[1])
            p.publish('/staj/arm2', val[2])
            p.publish('/staj/gripper', val[3])
            prevPotVals = val
        elif recordFlg:
            recorded.clear()
            for i in range(maxStep):
                print("Recording")
                val = pots.read()
                print(val)
                # servos.move(val, prevPotVals)
                recorded.append(val)
                if pauseBtn.value() == 1:
                    print("exit")
                    recorded.clear()
                    break
                sleep(.1)
                if recordBtn.value() == 1:
                    print("enough")
                    break
            recordFlg = False
        elif playFlg :
            if len(recorded) > 0:
                print("Playing record")
                for i in recorded:
                    print(i)
                    # servos.move(i, prevPotVals)
                    prevPotVals = i
                    if pauseBtn.value() == 1:
                        playFlg = False
                        break
                    sleep(.2)
            else:
                playFlg = False
            

        sleep(.2)