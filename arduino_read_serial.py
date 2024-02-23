import serial
import serial.tools.list_ports
import scamp  # http://scamp.marcevanstein.com/narrative/tutorial_videos.html

# from pathlib import Path
# current_path = str(Path().cwd())

# Get information from arduinos serial port.
def readserial(comport, baudrate) -> serial:
    return serial.Serial(comport, baudrate, timeout=0.1)  # 1/timeout is the frequency at which the port is read

# play_note(midi pitch value, volume 0-1, duration in seconds)
# 60 is middle C
# if data == "tone1":
#     piano.play_note(60, 0.8, 1) 
#     # continue
# elif data == "tone2":
#     piano.play_note(66, 0.8, 1)

# elif data == "tone3":
#     piano.play_note(50, 0.8, 1)
#     # continue
# elif data == "noTone":
#     # print(data)
#     print("Silence...")
#     # continue

# def pickInstrument() -> None:
#     pass

# def pickInstrument() -> None:
#     return None


# values_arduino = [play_tone, volume/100, instrument, durations, drum_sound, touchpad]

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
s = scamp.Session.run_as_server(self=s)  #COMMENT OUT IF TESTING
# s.print_default_soundfont_presets()
piano = s.new_part("Piano Merlin")
# piano.play_note(65, 1, 1)
# drums = s.new_part("Music Box")
# for i in tones_MIDI:
#     drums.play_note(i, 1, 1)



# Use function to get information from arduinos serial port.
ser = readserial(port, 9600)
while True:
    data = ser.readline().decode().strip()
    if data:
        # print(data)

        data_converted = str(data).split()
        print(data_converted)
        play_tone = float(data_converted[0])
        volume = float(data_converted[1])
        instrument = float(data_converted[2])
        durations = float(data_converted[3])
        drum_sound = float(data_converted[4])
        touchpad = float(data_converted[5])

        piano.play_note(play_tone, volume/100, durations)

