# Major
MAJOR = [2, 2, 1, 2, 2, 2]

# Minor
NATURAL_MINOR = [2, 1, 2, 2, 1, 2]
HARMONIC_MINOR = [2, 1, 2, 2, 1, 3]
MELODIC_MINOR = [2, 1, 2, 2, 2, 2]

# Blues
MINOR_BLUES = [3, 2, 1, 1, 3]
MAJOR_BLUES = [2, 1, 1, 3, 2]

# Pentatonic
MINOR_PENTATONIC = [3, 2, 2, 3]
MAJOR_PENTATONIC = [2, 2, 3, 2]

# World
ARABIC = [2, 2, 1, 1, 2, 2]
CHINESE = [4, 2, 1, 4]
EGYPTIAN = [2, 3, 2, 3]
ORIENTAL = [1, 3, 1, 1, 3, 1]


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
