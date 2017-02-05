#!/usr/bin/env python

import bob.pad.voice.database


# directory where the wave files are stored
asvspoof_input_dir = "/idiap/group/biometric/databases/pad/ASVspoof2017/ASVspoof2017_train_dev"
asvspoof_input_ext = ".wav"


database = bob.pad.voice.database.ASVspoof2017PadDatabase(
    protocol='competition',
    original_directory=asvspoof_input_dir,
    original_extension=asvspoof_input_ext,
    training_depends_on_protocol=True,
)
