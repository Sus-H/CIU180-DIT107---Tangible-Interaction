import serial
from pathlib import Path
import serial.tools.list_ports
import scamp

s = scamp.Session()
s = scamp.Session.run_as_server(self=s)
# s.timing_policy = 0.7
piano = s.new_part("piano")
# piano.play_note(65, 0.8, 1)

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
            piano.play_note(60, 0.8, 1)
            continue
        elif data == "tone2":
            piano.play_note(66, 0.8, 1)
            continue
        elif data == "noTone":
            # print(data)
            print("Silence...")
            continue


fromSerial = readserial(port, 9600)

