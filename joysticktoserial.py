import serial
import time
from time import sleep
from inputs import get_gamepad

lx = 200
ly = 200
rx = 200
ry = 200
LOW_TOL = 0.3
LOW_TOL2 = 0.5
HIGH_TOL = 0.9

delay = 10
currentTime = 0
pastTime = 0
msg = str('100100200003')
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM3'
print("Opening serial...")
ser.open()

def current_milli_time():
    return(round(time.time() * 1000))

def gamepad_events():
    global lx
    global ly
    global rx
    global msg
    events = get_gamepad()
    for event in events:
        if(event.code == 'ABS_X' and abs(round((event.state / 32767),2)) >= LOW_TOL):
            lx = round((event.state / 327.67),2) + 200
            print(lx)
        elif(event.code == 'ABS_X'):
            lx = 200
            print(lx)
        if(event.code == 'ABS_Y' and abs(round((event.state / 32767),2)) >= LOW_TOL):
            ly = -round((event.state / 327.67),2) + 200
            print(ly)
        elif(event.code == 'ABS_Y'):
            ly = 200
            print(ly)
        if(event.code == 'ABS_RX' and abs(round((event.state / 32767),2)) >= LOW_TOL2):
            rx = round((event.state / 400),2) + 200
            print(rx)
        elif(event.code == 'ABS_RX'):
            rx = 200
            print(rx)
    msg = (str(round(ly)) + str(round(lx)) + str(round(rx)) + str(100))

def print_serial():
    global currentTime
    global pastTime
    global delay
    global msg
    pastTime = current_milli_time()
    ser.write(msg.encode('utf-8'))
    print(msg)
    currentTime = current_milli_time()

while True:
    print_serial()
    gamepad_events()
    
#for future reference, every serial program requires a serial.close()
ser.close()
