import time
import serial
import serial.tools.list_ports
import pygame
from random import randint, choice
import mido
from math import sin, pi
import struct  # Import struct module for packing binary data
import sounddevice as sd

# Initialize Pygame mixer (without initializing Pygame)
pygame.mixer.init()

# Enumerate available audio devices
devices = sd.query_devices()

# Print information about each audio device
for idx, device in enumerate(devices):
    # if "game" in device["name"]:
        print(f"Device {idx}: {device['name']}")

# Select the desired output device (replace index with the desired device index)
output_device_index = 0  # Change this to the index of the desired output device
pygame.mixer.pre_init(devicename=devices[output_device_index]['name'])


# Initialize Pygame
pygame.init()

# FUNCTIONS ###############################################################
def read_serial(comport, baudrate):
    ''' Connects to Arduino '''

    return serial.Serial(comport, baudrate, timeout=0.1)

# Function to generate and play piano sound
def generate_piano_sound(frequency, duration, volume):
    sample_rate = 44100  # Sample rate (samples per second)

    # Calculate the number of samples
    num_samples = int(sample_rate * duration)

    # Generate the sound samples and scale them to fit in 16-bit signed integer range
    sound_samples = [int(volume * 32767 * sin(2 * pi * frequency * t / sample_rate)) for t in range(num_samples)]

    # Convert the samples to binary data
    sound_data = struct.pack('<' + 'h' * len(sound_samples), *sound_samples)

    # Create a Pygame sound object from the binary data
    sound = pygame.mixer.Sound(sound_data)

    # Play the sound
    print("Playing sound...")
    sound.play()

pygame.mixer.set_num_channels(16)


generate_piano_sound(261.63, 3, 0.5)
