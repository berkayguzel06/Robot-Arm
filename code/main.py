print("Main: RUN")
from mqtt import Pub, Rec
from potentio import Pots
from time import sleep
from machine import Pin
from servoMover import Servos

maxStep = 150 # Max step record
recorded = [] # Holds the current record
vals = [0,0,0,0] # Current values

# Connect sender to the server
p = Pub('Sender', 'serverName')
p.connect()
# Connect receivers to the server
baseR = Rec('baseReceiver', 'serverName','/topic/base')
arm1R = Rec('arm1Receiver', 'serverName','/topic/arm1')
arm2R = Rec('arm2Receiver', 'serverName','/topic/arm2')
gripperR = Rec('gripperReceiver', 'serverName','/topic/gripper')

# Initialize the servos
servos = Servos()
servos.attach(22) #base
servos.attach(23) #arm1
servos.attach(25) #arm2
servos.attach(26) #gripper

# Initialize the potentiometers
pots = Pots()
pots.attach(32) #base
pots.attach(33) #arm1
pots.attach(34) #arm2
pots.attach(35) #gripper

# Initialize the buttons
# Pause button helps to switch potentiometers to Node-Red
pauseBtn = Pin(18, Pin.IN)
pauseFlg = True
# Record button records the movements
recordBtn = Pin(19, Pin.IN)
recordFlg = False
# Play button plays the last record
playBtn = Pin(21,Pin.IN)
playFlg = False
playCount = 0
STAND_BY = 10 # seconds

def main():
    while True:
        if pauseFlg == True:
            potentioMove()
        elif pauseFlg == False and recordFlg == False and playFlg == False :
            noderedMove()
        elif recordFlg == True:
            record()
        elif playFlg == True:
            play()

def button():
    global recordBtn, pauseBtn, playBtn, pauseFlg, recordFlg, playFlg
    if recordBtn.value() == 1 and playFlg == False:
        pauseFlg = False
        recordFlg = True
    if playBtn.value() == 1 and recordFlg == False:
        pauseFlg = False
        playFlg = True
        
    if pauseBtn.value() == 1:
        if pauseFlg:
            print("Connecting to Broker")
            p.disconnect()
            baseR.connect()
            arm1R.connect()
            arm2R.connect()
            gripperR.connect()
            
            #syncroning receiver's values to sender's
            baseR.val = vals[0]
            arm1R.val = vals[1]
            arm2R.val = vals[2]
            gripperR.val = vals[3]
        else:
            p.connect()
            baseR.disconnect()
            arm1R.disconnect()
            arm2R.disconnect()
            gripperR.disconnect()

        pauseFlg = not pauseFlg

def potentioMove():
    print("Sending from potentiometers")
    global vals
    for i in range(maxStep):
        vals = pots.read()
        print(vals)
        servos.move(vals)
        p.publish('/topic/base', (str(vals[0]) + ',potentiometer'))
        p.publish('/topic/arm1', (str(vals[1]) + ',potentiometer'))
        p.publish('/topic/arm2', (str(vals[2]) + ',potentiometer'))
        p.publish('/topic/gripper', (str(vals[3]) + ',potentiometer'))
        button()
        sleep(.1)
        if i + 1 == maxStep:
            i = 0
        if pauseFlg == False:
            break    

def noderedMove():
    print("Recieving from Node-Red")
    global vals
    while not pauseFlg:
        baseR.receive()
        vals[0] = baseR.returnVal()
        arm1R.receive()
        vals[1] = arm1R.returnVal()
        arm2R.receive()
        vals[2] = arm2R.returnVal()
        gripperR.receive()
        vals[3] = gripperR.returnVal()
        print(vals)
        servos.move(vals)
        button()
        sleep(.1)

def record():
    recorded.clear()
    print("Recording")
    global recordFlg, pauseFlg
    for i in range(maxStep):
        vals = pots.read()
        recorded.append(vals)
        print(vals)
        servos.move(vals)
        sleep(.1)
        if pauseBtn.value() == 1:
            print("exit")
            recorded.clear()            
            break
        if recordBtn.value() == 1:
            print("enough")  
            break

    recordFlg = False
    pauseFlg = True
    sleep(.2)
def play():
    while playFlg:
        global playCount, playFlg, pauseFlg, recorded
        if len(recorded) > 0:
            print("Playing record")
            playCount +=1
            for i in recorded:
                print(i)
                servos.move(i)
                p.publish('/topic/base', (str(i[0]) + ',play'))
                p.publish('/topic/arm1', (str(i[1]) + ',play'))
                p.publish('/topic/arm2', (str(i[2]) + ',play'))
                p.publish('/topic/gripper', (str(i[3]) + ',play'))
                if pauseBtn.value() == 1:
                    pauseFlg = True
                    playFlg = False
                    break
                sleep(.1)
        else:
            pauseFlg = True
            playFlg = False
        
        if playCount > 2:
            print("-----COOLING-----")
            p.publish('/topic/status', "standby")         
            for j in range(2):
                for i in range(4095,2048,-100):
                    servos.move([i,4095,4095,4095])
                    sleep(.1)
            sleep(STAND_BY)
            p.publish('/topic/status', "active")         
            playCount = 0
    
if __name__ == "__main__":
    main()