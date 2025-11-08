# Scales

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

# 7 chords

SEVEN_CHORDS = {
    "MAJOR_SEVEN": [
        "MAJOR",
        "LYDIAN",
        "LYDIAN_SHARP_TWO"
    ],

    "MINOR_SEVEN": [
        "DORIAN",
        "PHRYGIAN",
        "NATURAL_MINOR",
        "DORIAN_FLAT_TWO",
        "DORIAN_SHARP_FOUR"
    ],
    
    "SEVEN": [
        "MIXOLYDIAN",
        "LYDIAN_DOMINANT",
        "AEOLIAN_DOMINANT",
        "PHRYGIAN_DOMINANT"
    ],

    "MINOR_SEVEN_FLAT_FIVE" : [
        "LOCRIAN",
        "HALF_DIMINISHED",
        "ALTERED",
        "LOCRIAN_NATURAL_SIX"
    ],

    "SEVEN_ALTERED" : [
        "ALTERED"
    ],

    "MINOR_MAJOR_SEVEN" : [
        "MELODIC_MINOR",
        "HARMONIC_MINOR"
    ],

    "MAJOR_SEVEN_SHARP_FIVE" : [
        "LYDIAN_AUGMENTED",
        "MAJOR_SHARP_FIVE"
    ],

    "DIMINISHED_SEVEN" : [
        "ALTERED_DOMINANT_DOUBLE_FLAT_SEVEN"
    ]
}


def generate_scale(tonic, scale, octaves):
    scale_notes = []
    octave = 0
    while octave < octaves:
        tonic_tmp = tonic + (12 * (octave))
        scale_notes += [tonic_tmp]
        for interval in scale:
            tonic_tmp += interval
            scale_notes += [tonic_tmp]
        octave += 1
    return scale_notes
