#!/usr/bin/env python

import bob.pad.voice.database


# directory where the wave files are stored
avspoof_input_dir = "/idiap/temp/pkorshunov/avspoof_cqcc/AVspoof_d3/btas2016/features/"
avspoof_input_ext = ".mat"


database = bob.pad.voice.database.AVspoofPadDatabase(
    protocol='grandtest',
    original_directory=avspoof_input_dir,
    original_extension=avspoof_input_ext,
    training_depends_on_protocol=True,
)
