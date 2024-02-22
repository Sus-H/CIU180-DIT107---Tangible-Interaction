import serial
from playsound import playsound
from pathlib import Path

def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read
    current_path = Path().cwd()

    while True:
        data = ser.readline().decode().strip()

        if data:
            print(data)
    
        if data == "tone1":
            audio = current_path / "sneeze.wav"
            playsound(audio)
        elif data == "tone2":
            audio = current_path / "failpiano.wav"
            playsound(audio)
            

fromSerial = readserial("COM11", 9600)