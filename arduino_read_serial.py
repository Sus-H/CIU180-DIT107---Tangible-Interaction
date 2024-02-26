import time
import serial
import serial.tools.list_ports
from scamp import Session
from random import randint, choice
from pprint import pprint
# http://scamp.marcevanstein.com/narrative/tutorial_videos.html

# from pathlib import Path
# current_path = str(Path().cwd())


# ///////////////////////// FUNCTIONS /////////////////////////////// #
# Get information from arduinos serial port.
# 1/timeout is the frequency at which the port is read
def read_serial(comport, baudrate):
    ''' Connects to Arduino '''

    return serial.Serial(comport, baudrate, timeout=0.1)


def play_drums(drum_picked, drum_pitch) -> None:
    '''plays the drums lmao'''
    actual_drums[drum_picked].play_note(drum_pitch, 1, 1/2)
    print(actual_drums[drum_picked])


# /////////////////////////// SETUP ////////////////////////////////// #
# Automatically get the correct port
ports = list(serial.tools.list_ports.comports())
for p in ports:
    # print(p.name)
    # print(p.description)

    if "Serial Device" or "Arduino" in p.description:
        print("This is an Arduino!")
        port = p.name
        print(port)


list_of_instr = ["Piano Merlin",
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
                 "acoustic bass"]

list_of_drums = ["Marimba",
                 "Xylophone",
                 "Reverse Cymbal"]


# Create a new "Music session" use run as server to suppress the error messages
main_session = Session()
drum_session = Session()
main_session.synchronization_policy = "no synchronization"
drum_session.synchronization_policy = "no synchronization"

for i in list_of_instr:
    main_session.add_instrument(main_session.new_part(i))
for i in list_of_drums:
    drum_session.add_instrument(drum_session.new_part(i))

# pprint(main_session.instruments[0:-1:2])
actual_instruments = main_session.instruments[0:-1:2]
actual_drums = drum_session.instruments[0:-1:2]
# pprint(drum_session.instruments)
# pprint(actual_drums)


# ///////////////////////// TEST BLOCK /////////////////////////////// #
TESTING = False

tones_midi = [60, 62, 64, 65, 67, 69, 71, 72]
if TESTING is True:
    for picked_instr in actual_instruments:
        for tone in tones_midi:
            drum_session.fork(process_function=play_drums, args=[2, 60])
            picked_instr.play_note(tone, 0.3, 1/2)  # parent sesh
            print(picked_instr)
            # time.sleep(500)


# ///////////////////////// MAIN /////////////////////////////// #
# Use function to get information from arduinos serial port.
if TESTING is not True:
    ser = read_serial(port, 9600)
    main_session = Session.run_as_server(self=main_session)
    drum_session = Session.run_as_server(self=drum_session)
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
            volume = data_converted[1]/100
            instr = actual_instruments[data_converted[2]]
            print(list_of_instr[data_converted[2]])
            durations = data_converted[3]
            print(durations/64)
            drum_picked = data_converted[4]
            touchpad = data_converted[5]

            print([play_tone,
                   volume,
                   instr,
                   durations,
                   drum_picked,
                   touchpad])

            if not play_tone:
                volume = 0
            instr.play_note(pitch=play_tone,
                            volume=volume,
                            length=durations/64)

            if touchpad:
                drum_session.fork(process_function=play_drums,
                                  args=[drum_picked, play_tone])            
