import serial
from playsound import playsound
import multiprocessing



def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        data = ser.readline().decode().strip()
        # if data:
        #     print(data)
    
        if data == "Hello":
            p = multiprocessing.Process(target=playsound, args=("sneeze.wav",))
            p.start()
            input("press ENTER to stop playback")
            p.terminate()


fromSerial = readserial("COM5", 9600)








