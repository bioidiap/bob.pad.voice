#!/usr/bin/env python

import bob.bio.base.database


# directory where the wave files are stored
# asvspoof_input_dir = "/idiap/resource/database/mobio/denoisedAUDIO_16k/"  #MOBIO database for UBM training
asvspoof_input_dir = "/idiap/resource/database/ASVspoof2015/ASVspoof2015_development"  #Path to ASVspoof in Idiap
# asvspoof_input_dir = "/Users/pavelkor/Documents/pav/idiap/data/asvspoof"  #path to a local copy
asvspoof_input_ext = ".wav"


database_licit = bob.bio.base.database.ASVspoofBioDatabase(
    protocol='licit',
    original_directory=asvspoof_input_dir,
    original_extension=asvspoof_input_ext,
    training_depends_on_protocol=True,
)

database_spoof = bob.bio.base.database.ASVspoofBioDatabase(
    protocol='spoof',
    original_directory=asvspoof_input_dir,
    original_extension=asvspoof_input_ext,
    training_depends_on_protocol=True,
)
