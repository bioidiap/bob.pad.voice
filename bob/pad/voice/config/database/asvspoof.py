#!/usr/bin/env python

import bob.pad.voice.database


# directory where the wave files are stored
asvspoof_input_dir = "/idiap/resource/database/ASVspoof2015/ASVspoof2015_development"  #Path to ASVspoof in Idiap
# asvspoof_input_dir = "/Users/pavelkor/Documents/pav/idiap/data/asvspoof"  #path to a local copy
asvspoof_input_ext = ".wav"


database = bob.pad.voice.database.ASVspoofPadDatabase(
    protocol='CM',
    original_directory=asvspoof_input_dir,
    original_extension=asvspoof_input_ext,
    training_depends_on_protocol=True,
)
