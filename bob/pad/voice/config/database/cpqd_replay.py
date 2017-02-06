#!/usr/bin/env python

from bob.pad.voice.database import CPqDReplayPadDatabase


# directory where the wave files are stored
cpqd_input_dir = "[YOUR_CPQD_WAV_DIRECTORY]"
cpqd_input_ext = ".wav"


database = CPqDReplayPadDatabase(
    protocol='cpqdlspk1',
    original_directory=cpqd_input_dir,
    original_extension=cpqd_input_ext,
    training_depends_on_protocol=True,
)
