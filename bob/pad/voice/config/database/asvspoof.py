#!/usr/bin/env python

import bob.pad.voice.database


# directory where the wave files are stored
asvspoof_input_dir = "/idiap/temp/pkorshunov/avspoof_cqcc/ASVspoof_d3"
asvspoof_input_ext = ".mat"


database = bob.pad.voice.database.ASVspoofPadDatabase(
    protocol='CM',
    original_directory=asvspoof_input_dir,
    original_extension=asvspoof_input_ext,
    training_depends_on_protocol=True,
)
