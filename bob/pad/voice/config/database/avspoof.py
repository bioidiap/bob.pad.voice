#!/usr/bin/env python

import bob.pad.voice.database


# directory where the wave files are stored
# avspoof_input_dir = "/idiap/project/lobi/AVSpoof/data/"  # folder at Idiap
avspoof_input_dir = "/Users/pavelkor/Documents/pav/idiap/data/AVspoof_full/data/"  # local copy
avspoof_input_ext = ".wav"


database = bob.pad.voice.database.AVspoofPadDatabase(
    protocol='smalltest',
    original_directory=avspoof_input_dir,
    original_extension=avspoof_input_ext,
    training_depends_on_protocol=True,
)
