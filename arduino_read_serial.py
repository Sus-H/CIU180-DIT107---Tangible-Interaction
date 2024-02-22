import serial
import serial.tools.list_ports
import scamp # http://scamp.marcevanstein.com/narrative/tutorial_videos.html

# from pathlib import Path
# current_path = str(Path().cwd())

# Get information from arduinos serial port.
def readserial(comport, baudrate):
    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        data = ser.readline().decode().strip()

        if data:
            print(data)

        # play_note(midi pitch value, volume 0-1, duration in seconds)
        # 60 is middle C
        if data == "tone1":
            piano.play_note(60, 0.8, 1) 
            # continue
        elif data == "tone2":
            piano.play_note(66, 0.8, 1)
            # continue
        elif data == "noTone":
            # print(data)
            print("Silence...")
            # continue

# Automatically get the correct port
ports = list(serial.tools.list_ports.comports())
for p in ports:
    # print(p.name)
    if "Serial Device" in p.description:
        print("This is an Arduino!")
        port = p.name
        print(port)

# Create a new "Music session" and use run as server to suppress the error messages 
s = scamp.Session()
# s = scamp.Session.run_as_server(self=s)
piano = s.new_part("piano")
piano.play_note(65, 1, 1)

# Use function to get information from arduinos serial port.
# fromSerial = readserial(port, 9600)