# Scales

import notes

SCALES = {
    # Major modes
    "MAJOR": [2, 2, 1, 2, 2, 2],
    "DORIAN": [2, 1, 2, 2, 2, 1],
    "PHRYGIAN": [1, 2, 2, 2, 1, 2],
    "LYDIAN": [2, 2, 2, 1, 2, 2, 1],
    "MIXOLYDIAN": [2, 2, 1, 2, 2, 1, 2],
    "NATURAL_MINOR": [2, 1, 2, 2, 1, 2, 2],
    "LOCRIAN": [1, 2, 2, 1, 2, 2, 2],

    # Melodic Minor modes
    "MELODIC_MINOR": [2, 1, 2, 2, 2, 2],
    "DORIAN_FLAT_TWO": [1, 2, 2, 2, 2, 1],
    "LYDIAN_AUGMENTED": [2, 2, 2, 2, 1, 2],
    "LYDIAN_DOMINANT": [2, 2, 2, 1, 2, 1],
    "AEOLIAN_DOMINANT": [2, 2, 1, 2, 1, 2],
    "HALF_DIMINISHED": [2, 1, 2, 1, 2, 2],
    "ALTERED": [1, 2, 1, 2, 2, 2],

    # Harmonic Minor modes
    "HARMONIC_MINOR": [2, 1, 2, 2, 1, 3],
    "LOCRIAN_NATURAL_SIX": [1, 2, 2, 1, 3, 2],
    "MAJOR_SHARP_FIVE": [2, 2, 1, 3, 2, 1],
    "DORIAN_SHARP_FOUR": [2, 1, 3, 2, 1, 2],
    "PHRYGIAN_DOMINANT": [1, 3, 2, 1, 2, 2],
    "LYDIAN_SHARP_TWO": [3, 2, 1, 2, 2, 1],
    "ALTERED_DOMINANT_DOUBLE_FLAT_SEVEN": [2, 1, 2, 2, 1, 3],

    # Harmonic Major modes
    "HARMONIC_MAJOR": [2, 2, 1, 2, 1, 3],
    "DORIAN_FLAT_FIVE": [2, 1, 2, 1, 3, 2],
    "PHRYGIAN_FLAT_FOUR": [1, 2, 1, 3, 2, 2],
    "LYDIAN_FLAT_THREE": [2, 1, 3, 2, 2, 1],
    "MIXOLYDIAN_FLAT_TWO": [1, 3, 2, 2, 1, 2],
    "LYDIAN_AUGMENTED_SHARP_TWO": [3, 2, 2, 1, 2, 1],
    "LOCRIAN_DOUBLE_FLAT_SEVEN": [3, 2, 2, 1, 2, 1],

    # Diminished modes
    "DIMINISHED": [2, 1, 2, 1, 2, 1],
    "INVERTED_DIMINISHED": [1, 2, 1, 2, 1, 2],

    # Whole Tone mode
    "WHOLE_TONE": [2, 2, 2, 2, 2],

    # Augmented modes
    "AUGMENTED": [3, 1, 3, 1, 3],
    "INVERTED_AUGMENTED": [1, 3, 1, 3, 1],

    # SPECIAL

    # Blues
    "MINOR_BLUES": [3, 2, 1, 1, 3],
    "MAJOR_BLUES": [2, 1, 1, 3, 2],

    # Pentatonic
    "MINOR_PENTATONIC": [3, 2, 2, 3],
    "MAJOR_PENTATONIC": [2, 2, 3, 2],

    # World
    "ARABIC": [2, 2, 1, 1, 2, 2],
    "CHINESE": [4, 2, 1, 4],
    "EGYPTIAN": [2, 3, 2, 3],
    "ORIENTAL": [1, 3, 1, 1, 3, 1]
}

# Chords

CHORDS = {
    "MAJOR_SEVEN": {
        "scales": [
            "MAJOR",
            "LYDIAN",
            "LYDIAN_SHARP_TWO",
            "HARMONIC_MAJOR",
            "AUGMENTED"
        ],
        "intervals": [
            4,
            3,
            4
        ]
    },
    "MINOR_SEVEN": {
        "scales": [
            "DORIAN",
            "PHRYGIAN",
            "NATURAL_MINOR",
            "DORIAN_FLAT_TWO",
            "DORIAN_SHARP_FOUR",
            "PHRYGIAN_FLAT_FOUR"
        ],
        "intervals": [
            3,
            4,
            3
        ]
    },
    "SEVEN": {
        "scales": [
            "MIXOLYDIAN",
            "LYDIAN_DOMINANT",
            "AEOLIAN_DOMINANT",
            "PHRYGIAN_DOMINANT",
            "PRYGIAN_FLAT_FOUR",
            "MIXOLYDIAN_FLAT_TWO",
            "INVERTED_DIMINISHED"
        ],
        "intervals": [
            4,
            3,
            3
        ]
    },
    "MINOR_SEVEN_FLAT_FIVE": {
        "scales": [
            "LOCRIAN",
            "HALF_DIMINISHED",
            "ALTERED",
            "LOCRIAN_NATURAL_SIX",
            "DORIAN_FLAT_FIVE"
        ],
        "intervals": [
            3,
            3,
            4
        ]
    },
    "SEVEN_ALTERED": {
        "scales": [
            "ALTERED"
        ],
        "intervals": [
            4,
            3,
            3
        ]
    },
    "MINOR_MAJOR_SEVEN": {
        "scales": [
            "MELODIC_MINOR",
            "HARMONIC_MINOR",
            "LYDIAN_FLAT_THREE"
        ],
        "intervals": [
            3,
            4,
            4
        ]
    },
    "MAJOR_SEVEN_SHARP_FIVE": {
        "scales": [
            "LYDIAN_AUGMENTED",
            "MAJOR_SHARP_FIVE",
            "LYDIAN_AUGMENTED_SHARP_TWO"
        ],
        "intervals": [
            4,
            4,
            3
        ]
    },
    "DIMINISHED_SEVEN": {
        "scales": [
            "ALTERED_DOMINANT_DOUBLE_FLAT_SEVEN",
            "LOCRIAN_DOUBLE_FLAT_SEVEN",
            "DIMINISHED"
        ],
        "intervals": [
            3,
            3,
            3
        ]
    },
    "SEVEN_FLAT_FIVE_SHARP_FIVE": {
        "scales": [
            "WHOLE_TONE"
        ],
        "intervals": [
            4,
            2,
            3
        ]
    },
    "SIX_SHARP_FIVE": {
        "scales": [
            "INVERTED_AUGMENTED"
        ],
        "intervals": [
            4,
            4,
            3
        ]
    }
}


def generate_scale(note_name: str, start_octave: int, scale_name: str, total_octaves: int = 1):
    scale = SCALES[scale_name]
    return __generate_scale(note_name=note_name, start_octave=start_octave,
                            scale=scale, total_octaves=total_octaves)


def __generate_scale(note_name: str, start_octave: int, scale: list, total_octaves: int = 1):
    scale_notes = []
    octave = 0
    tonic_midi_number = notes.NOTES[note_name][start_octave]["midi_number"]
    while octave < total_octaves:
        tonic_tmp = tonic_midi_number + (12 * (octave))
        scale_notes += [tonic_tmp]
        for interval in scale:
            tonic_tmp += interval
            scale_notes += [tonic_tmp]
        octave += 1
    return scale_notes


def generate_chord(note_name: str, start_octave: int, chord_name: str):
    chord = CHORDS[chord_name]["intervals"]
    return __generate_scale(note_name=note_name, start_octave=start_octave,
                            scale=chord)
