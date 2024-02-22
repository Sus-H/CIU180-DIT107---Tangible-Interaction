import serial
from playsound import playsound
from pathlib import Path
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
for p in ports:
    # print(p.name)

    if "Serial Device" in p.description:
        print("This is an Arduino!")
        port = p.name
        print(port)

def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read
    current_path = str(Path().cwd())

    while True:
        data = ser.readline().decode().strip()

        if data:
            print(data)
    
        if data == "tone1":
            audio = current_path + "\sneeze.wav"
            playsound(audio)
        elif data == "tone2":
            audio = current_path + "\pianofail.wav"
            playsound(audio)
        elif data == "noTone":
            print("Silence...")


fromSerial = readserial(port, 9600)