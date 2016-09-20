
#!/usr/bin/env python

import bob.bio.base.database

# directory where the wave files are stored
avspoof_input_dir = "/idiap/project/lobi/AVSpoof/data/"
# avspoof_input_dir = "/Users/pavelkor/Documents/pav/idiap/data/AVspoof_full/data/"
avspoof_input_ext = ".wav"


database_licit = bob.bio.base.database.AVspoofBioDatabase(
    protocol='licit',
    original_directory=avspoof_input_dir,
    original_extension=avspoof_input_ext,
    training_depends_on_protocol=True,
)

database_spoof = bob.bio.base.database.AVspoofBioDatabase(
    protocol='spoof',
    original_directory=avspoof_input_dir,
    original_extension=avspoof_input_ext,
    training_depends_on_protocol=True,
)
