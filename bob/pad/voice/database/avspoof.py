#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Pavel Korshunov <pavel.korshunov@idiap.ch>
# Tue 17 May 15:43:22 CEST 2016

"""
  This is a high level interface for presentation attack AVspoof database.
  It is an extension of an interface defined inside bob.pad.base PAD framework.
"""

from bob.pad.voice.database import PadVoiceFile
from bob.pad.base.database import PadDatabase


class AVspoofPadFile(PadVoiceFile):
    def __init__(self, f):
        """
        Initializes this File object with an File equivalent from the underlying SQl-based interface for
        AVspoof database.
        """
        attacktype = None
        if f.is_attack():
            attacktype = str(f.get_attack())

        super(AVspoofPadFile, self).__init__(client_id=f.client_id, path=f.path, attack_type=attacktype, file_id=f.id)

        self.__f = f


class AVspoofPadDatabase(PadDatabase):
    """
    Implements verification API for querying AVspoof database.
    """

    def __init__(self, protocol='grandtest', **kwargs):
        # call base class constructors to open a session to the database
        PadDatabase.__init__(self, name='avspoof', protocol=protocol, **kwargs)

        from bob.db.avspoof.query import Database as LowLevelDatabase
        self.__db = LowLevelDatabase()

        # Since the high level API expects different group names than what the low
        # level API offers, you need to convert them when necessary
        self.low_level_group_names = ('train', 'devel', 'test')
        self.high_level_group_names = ('train', 'dev', 'eval')

    def objects(self, groups=None, protocol=None, purposes=None, model_ids=None, **kwargs):
        """Returns a set of Files for the specific query by the user.

        Keyword Parameters:

        groups
            One of the groups ('dev', 'eval', 'train') or a tuple with several of them.
            If 'None' is given (this is the default), it is considered the same as a
            tuple with all possible values.

        protocol
          The protocol for which the clients should be retrieved.
          The protocol is dependent on your database.
          If you do not have protocols defined, just ignore this field.

        purposes
            The purposes can be either 'real' or 'attack'.

        model_ids
            This parameter is not supported in this implementation.


        Returns: A set of Files with the specified properties.
        """
        # convert group names from the conventional in PAD experiments to the internal database names
        matched_groups = self.convert_names_to_lowlevel(
            groups, self.low_level_group_names, self.high_level_group_names)

        objects = self.__db.objects(protocol=protocol, groups=matched_groups, cls=purposes, **kwargs)
        return [AVspoofPadFile(f) for f in objects]

    def annotations(self, file):
        return None
