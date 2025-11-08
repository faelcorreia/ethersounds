import mido
import time
import random
import scales
import sys
import json
import notes
from threading import Thread


def choose_port():
    print("Listing ports:")
    chosen = False
    midi_port = ""
    while not chosen:
        i = 1
        id = 0
        outputs = mido.get_output_names()
        for port in outputs:
            print("[{0}] {1}".format(i, port))
            i += 1

        sys.stdout.write("Choose the output: ")
        try:
            id = int(input())
            if id > 0 and id < i:
                midi_port = outputs[id-1]
                chosen = True
            else:
                print("Invalid id!")
        except ValueError:
            print("Not a number!")
    return midi_port


def play_note(note, delay):
    msg_on = mido.Message('note_on', note=note)
    msg_off = mido.Message('note_off', note=note)
    port.send(msg_on)
    time.sleep(delay)
    port.send(msg_off)


def play_eternal_note(note):
    msg_on = mido.Message('note_on', note=note)
    port.send(msg_on)


def play_random(start, end, delay):
    while True:
        note = random.randint(start, end)
        play_note(note, delay)


def play_scale(note, scale, delay, octaves=1):
    scale = scales.generate_scale(note, scale, octaves)
    while True:
        for note in scale:
            play_note(note, delay)


def play_random_in_scale(note, scale, delay, octaves=1, same_time=1):
    scale = scales.generate_scale(note, scale, octaves)
    size = len(scale)
    while True:
        i = 0
        while i < same_time:
            note = scale[random.randint(0, size-1)]
            thread = Thread(target=play_note, args=(note, delay))
            thread.start()
            i += 1
        time.sleep(delay)


def play_random_pattern(note, number_of_notes, scale, delay, octaves=1):
    scale = scales.generate_scale(note, scale, octaves)
    pattern = []
    i = 0
    size = len(scale)
    while i < number_of_notes:
        note = scale[random.randint(0, size-1)]
        pattern += [note]
        i += 1
    while True:
        for note in pattern:
            play_note(note, delay)


if __name__ == '__main__':
    midi_port = choose_port()
    with mido.open_output(midi_port) as port:
        # play_random_pattern(notes.A_2, 8, scales.MINOR_PENTATONIC, random.randint(1, 5), octaves=1)
        play_random_in_scale(
            note=notes.NOTES["C"][2]["midi_number"], scale=scales.SCALES["MINOR_PENTATONIC"], delay=0.3, octaves=2, same_time=2)
