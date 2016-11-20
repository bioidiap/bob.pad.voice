#!/usr/bin/env python

from bob.pad.voice.database import CPqDReplayPadDatabase


# directory where the wave files are stored
voicepa_input_dir = "[YOUR_CPQDREPLAY_WAV_DIRECTORY]"
voicepa_input_ext = ".wav"


database = CPqDReplayPadDatabase(
    protocol='cpqdlspk1',
    original_directory=voicepa_input_dir,
    original_extension=voicepa_input_ext,
    training_depends_on_protocol=True,
)
