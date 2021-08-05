import time
import serial
import socket
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)

ser = serial.Serial(port ='/dev/serial0', baudrate = 9600 , parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)
temp=''

while True:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('169.254.199.57',5005))
    string = "Receiver is active"
    msg = bytes(string,'utf-8')
    client.send(msg)
    from_server = client.recv(4096)
    from_server = from_server.decode('utf-8')
    if(from_server=='%#%#%#'):
     client.close()
     close1='%#%#%#'
     close2=close1.encode('utf-8')
     ser.write(close2)
     ser.close()
     break
    else:
        if(from_server=='onLed'):
            GPIO.output(11,GPIO.HIGH)
        elif(from_server=='offLed'):
            GPIO.output(11,GPIO.LOW)
        from_server=from_server+'$'
        msgInBytes = from_server.encode('utf-8')
        ser.write(msgInBytes)
        mread=ser.read(1)
        temp=mread.decode('utf-8')#print(temp)
        if(temp=='y'):
            print('RECIEVED!')
            continue
       
    
        #time.sleep(0.13)
