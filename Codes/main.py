print("Main: RUN")
from machine import Pin,I2C
from time import sleep
from mqtt import Pub, Rec
from pca9685 import PCA9685
from potentio import Pots
from servo import Servos
from SCARA import SCARA

maxStep = 150 # Max step record
recorded = [] # Holds the current record
vals = [0,0,0,0] # Current values

# Connect sender to the server
p = Pub('robot', 'serverName')
p.connect()

# Connect scara sender
s = Pub('scara', 'serverName')

# Connect receivers to the server
baseR = Rec('baseReceiver', 'serverName','/topic/base')
arm1R = Rec('arm1Receiver', 'serverName','/topic/arm1')
arm2R = Rec('arm2Receiver', 'serverName','/topic/arm2')
gripperR = Rec('gripperReceiver', 'serverName','/topic/gripper')

#I2C reqs
sda = Pin(16)
scl = Pin(17)

i2c = I2C(sda=sda, scl=scl)
pca = PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)

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

#Gripper move button
gripperBtn = Pin(25)
gripperFlg = False

# Play button plays the last record
playBtn = Pin(21,Pin.IN)
playFlg = False
playCount = 0
STAND_BY = 10 # seconds
#change robot
changeBtn = Pin(22, Pin.IN)
changeFlg = False

#scara
scara = SCARA()

def main():
    while True:
        if pauseFlg == True:
            potentioMove()
        if changeFlg == True:
            scara_potentio()
        if pauseFlg == False and recordFlg == False and playFlg == False and changeFlg == False:
            noderedMove()
        if recordFlg == True:
            record()
        if playFlg == True:
            play()
        
def scara_potentio():
    global pauseFlg, changeFlg, pauseBtn
    while True:
        ret_list = scara.potentioMove(pots.filtered_read())
        
        if pauseBtn.value() == 1:
            pauseFlg = True
            changeFlg = False
            break
        
        if ret_list == None:
            continue
        
        s.publish(ret_list[0],ret_list[1])
        s.publish(ret_list[0]+'Position',ret_list[2])
        
        print("---------------")
        print(ret_list[0]+'Position')
        print("pot")
        print(ret_list[3])
        print("mapped")
        print(ret_list[4])
        print("motor")
        print(ret_list[5])
        print("---------------")

        sleep(.1)
    ret_list = scara.safe_exit()
    s.publish(ret_list[0],ret_list[1])
    s.publish(ret_list[2],ret_list[3])
    s.publish(ret_list[4],ret_list[5])
    
    s.publish(ret_list[0]+'Position',0)
    s.publish(ret_list[2]+'Position',0)
    s.publish(ret_list[4]+'Position',0)
    s.disconnect()
    p.connect()

def button():
    global recordBtn, pauseBtn, playBtn, pauseFlg, recordFlg, playFlg, changeFlg
    if recordBtn.value() == 1 and playFlg == False:
        pauseFlg = False
        recordFlg = True
    elif changeBtn.value() == 1:
        if pauseFlg == True:
            pauseFlg = False
            changeFlg = True
            s.connect()
            p.disconnect()
            
    elif playBtn.value() == 1 and recordFlg == False:
        pauseFlg = False
        playFlg = True
        
    elif pauseBtn.value() == 1:
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

        #Read gripper button
        _gripperMove()

        _moveServo(vals)
        
        #mqtt publish
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
    global vals, pauseFlg
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
        _moveServo(vals)
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
        _moveServo(vals)
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
                _moveServo(i)
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

def _map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def _moveServo(vals):
    servo.position(index=0, degrees=_map_range(vals[0],0,4095 ,30 ,150))
    servo.position(index=1, degrees=_map_range(vals[1],0,4095 ,20 ,180))
    servo.position(index=2, degrees=_map_range(vals[2],0,4095 ,180 ,0))
    servo.position(index=4, degrees=_map_range(vals[3],0,4095 ,0 ,180))

def _gripperMove():
    global gripperBtn,gripperFlg
    if gripperBtn.value() == 1:
        if not gripperFlg:
            gripperFlg = True
            servo.position(index=5, degrees=90)
        else:
            gripperFlg = False
            servo.position(index=5, degrees=180)

if __name__ == "__main__":
    main()