import time
import serial
import serial.tools.list_ports
from scamp import Session
from random import randint, choice
from pprint import pprint
# http://scamp.marcevanstein.com/narrative/tutorial_videos.html

# from pathlib import Path
# current_path = str(Path().cwd())

# Get information from arduinos serial port.
# 1/timeout is the frequency at which the port is read
def read_serial(comport, baudrate):
    ''' Connects to Arduino '''

    return serial.Serial(comport, baudrate, timeout=0.1)


def play_drums(drum_picked=1, drum_pitch=60) -> None:
    '''plays the drums lmao'''
    drum_session.instruments[drum_picked].play_note(drum_pitch, 1, 1/2)


# Automatically get the correct port
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p.name)
    port = p.name

    # if "Serial Device" in p.description:
    #     print("This is an Arduino!")
    #     port = p.name
    #     print(port)

list_of_instr = ["Glockenspiel",
                 "Shamisen",
                 "Banjo",
                 "Piano Merlin",
                 "ocarina",
                 "bandoneon",
                 "dulcimer",
                 "oboe",
                 "TR 808",
                 "clean guitar",
                 "Distortion Guitar",
                 "acoustic bass",]

list_of_drums = ["Steel Drum",
                 "Taiko Drum",
                 "Synth Drum"]

# Create a new "Music session" use run as server to suppress the error messages
main_session = Session()
drum_session = Session()

for i in list_of_instr:
    main_session.add_instrument(main_session.new_part(i))
for i in list_of_drums:
    drum_session.add_instrument(drum_session.new_part(i))

# pprint(main_session.instruments[0:-1:2])
actual_instruments = main_session.instruments[0:-1:2]
# pprint(actual_instruments)
tones_midi = [60, 62, 64, 65, 67, 69, 71, 72]
TESTING = False
if TESTING is True:
    for picked_instr in actual_instruments:
        for tone in tones_midi:
            drum_session.fork(play_drums)
            picked_instr.play_note(tone, 0.3, 1/4)  # parent sesh

# Use function to get information from arduinos serial port.
if TESTING is not True:
    ser = read_serial(port, 9600)
    main_session = Session.run_as_server(self=main_session)
    durations = 1/2
    while True:
        data = ser.readline().decode().strip()
        # data = "this is incoming data"
        # main_session.fast_forward(0)
        if data:
            data_converted = str(data).split(" ")
            data_converted = [int(i) for i in data_converted]
            # data_converted: list[int | float] = [choice([60, 64, 67]),
            #                                      10,
            #                                      0,
            #                                      1/32,
            #                                      2,
            #                                      randint(1, 1)]
            print(data_converted)

            play_tone = data_converted[0]
            volume = data_converted[1]
            instr = actual_instruments[data_converted[2]]
            print(list_of_instr[data_converted[2]])
            durations = data_converted[3]
            print(durations/64)
            drum = drum_session.instruments[data_converted[4]]
            touchpad = data_converted[5]

            if not play_tone:
                volume = 0
            instr.play_note(pitch=play_tone,
                            volume=volume/100,
                            length=durations/64,
                            blocking=False)

            if touchpad:
                drum_session.fork(play_drums)
