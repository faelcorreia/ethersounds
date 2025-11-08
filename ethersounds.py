import mido
import time
import random
import scales
import sys
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


def play_jazz_improvisation():
    chords = [
        ("D", "MINOR_SEVEN_FLAT_FIVE"),
        ("G", "SEVEN"),
        ("C", "MINOR_MAJOR_SEVEN")
    ]

    chord_octave = 3
    start_octave_improvisation = 4
    end_octave_improvisation = 5
    maximum_octaves = 2
    total_notes = 32
    delay = 0.1
    i = 0
    chords_size = len(chords)

    while True:
        rand_octave = random.randint(
            start_octave_improvisation, end_octave_improvisation)
        rand_octaves = random.randint(1, maximum_octaves)
        chord = chords[i]
        note_name = chord[0]
        chord_name = chord[1]
        chord_scales = scales.CHORDS[chord_name]["scales"]
        chord_intervals = scales.CHORDS[chord_name]["intervals"]

        # Generating random scale
        rand_scale_name = chord_scales[random.randint(
            0, len(chord_intervals)-1)]
        scale = scales.generate_scale(
            note_name=note_name, start_octave=rand_octave, scale_name=rand_scale_name, total_octaves=rand_octaves)
        scale_size = len(scale)

        # Getting chord notes
        chord_scale = scales.generate_chord(
            note_name=note_name, start_octave=chord_octave, chord_name=chord_name)
        chord_scale_size = len(chord_scale)

        # Play seven chord
        print(f"Playing {note_name}_{chord_name} ({chord_octave}) chord...")
        for j in range(0, chord_scale_size):
            note = chord_scale[j]
            thread = Thread(target=play_note, args=(note, delay*total_notes))
            thread.start()

        # Improvise in random scale
        print(
            f"Improvising over {note_name}_{rand_scale_name} ({start_octave_improvisation}-{end_octave_improvisation}) scale...")
        rand_start = random.randint(0, scale_size - 1)
        for k in range(0, total_notes):
            note = scale[(k+rand_start) % scale_size]
            thread = Thread(target=play_note, args=(note, delay))
            thread.start()
            time.sleep(delay)
        print()

        i += 1
        i %= chords_size


if __name__ == '__main__':
    midi_port = choose_port()
    with mido.open_output(midi_port) as port:
        # play_random_pattern(notes.A_2, 8, scales.MINOR_PENTATONIC, random.randint(1, 5), octaves=1)
        # play_random_in_scale(note="C_2", scale="MINOR_PENTATONIC", delay=0.3, octaves=2, same_time=2)
        play_jazz_improvisation()
