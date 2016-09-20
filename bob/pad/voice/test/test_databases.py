#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavel.korshunov@idiap.ch>
# @date: Thu Apr 21 16:41:21 CEST 2016
#
# Copyright (C) 2011-2012 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import unittest
import bob.pad.base

import pkg_resources

dummy_dir = pkg_resources.resource_filename('bob.pad.voice', 'test/dummy')


class DummyDatabaseTest(unittest.TestCase):
    """Performs various tests on the AVspoof attack database."""

    def test00_db_available(self):
        db = bob.bio.base.load_resource(os.path.join(dummy_dir, 'database.py'), 'database',
                                            package_prefix='bob.pad.')
        self.assertTrue(db)

    def test01_trainFiles(self):
        db = bob.bio.base.load_resource(os.path.join(dummy_dir, 'database.py'), 'database', package_prefix='bob.pad.')
        files = db.all_files(groups='train')
        self.assertEqual(len(files), 2)
        names = db.original_file_names(files)
        self.assertEqual(len(names), 2)
        print (names)
        self.assertTrue(('attack_laptop_sentence01' in names[1]))
        self.assertTrue(('genuine_laptop_sentence01' in names[0]))

    # @db_available
    def test02_devFiles(self):
        db = bob.bio.base.load_resource(os.path.join(dummy_dir, 'database.py'), 'database', package_prefix='bob.pad.')
        files = db.all_files(groups='dev')
        self.assertEqual(len(files), 2)
        names = db.original_file_names(files)
        self.assertEqual(len(names), 2)
        self.assertTrue(('attack_phone_sentence01' in names[1]))
        self.assertTrue(('genuine_laptop2_sentence01' in names[0]))

    # @db_available
    def test03_evalFiles(self):
        db = bob.bio.base.load_resource(os.path.join(dummy_dir, 'database.py'), 'database', package_prefix='bob.pad.')
        files = db.all_files(groups='eval')
        self.assertEqual(len(files), 2)
        names = db.original_file_names(files)
        self.assertEqual(len(names), 2)
        self.assertTrue(('attack_ss_sentence01' in names[1]))
        self.assertTrue(('genuine_phone_sentence01' in names[0]))

    # @db_available
    def test04_trainFiles4Test(self):
        db = bob.bio.base.load_resource(os.path.join(dummy_dir, 'database.py'), 'database', package_prefix='bob.pad.')
        files = db.all_files(groups='train')
        self.assertEqual(len(files), 2)
        names = db.original_file_names(files)
        self.assertEqual(len(names), 2)
        self.assertTrue(('attack_laptop_sentence01' in names[1]))
        self.assertTrue(('genuine_laptop_sentence01' in names[0]))

    # @db_available
    def test05_scoreFiles(self):
        db = bob.bio.base.load_resource(os.path.join(dummy_dir, 'database.py'), 'database', package_prefix='bob.pad.')
        files = db.all_files(groups='train')
        self.assertEqual(len(files), 2)
        names = db.original_file_names(files)
        self.assertEqual(len(names), 2)
        self.assertTrue(('attack_laptop_sentence01' in names[1]))
        self.assertTrue(('genuine_laptop_sentence01' in names[0]))

    # @db_available
    def test06_getAllData(self):
        db = bob.bio.base.load_resource(os.path.join(dummy_dir, 'database.py'), 'database', package_prefix='bob.pad.')
        self.assertEqual(len(db.all_files(groups='train')), 2)
        self.assertEqual(len(db.all_files(groups='dev')), 2)
        self.assertEqual(len(db.all_files(groups='eval')), 2)
        self.assertEqual(len(db.all_files(groups=('train, dev, eval'))[1]), 3)
        self.assertEqual(len(db.all_files(groups=('train, dev, eval'))[0]), 3)

    # @db_available
    def test07_manage_files(self):
        from bob.db.base.script.dbmanage import main

        self.assertEqual(main('speech_spoof_test files'.split()), 0)

    # @db_available
    def test08_manage_dumplist(self):
        from bob.db.base.script.dbmanage import main

        self.assertEqual(main('speech_spoof_test dumplist --self-test'.split()), 0)
