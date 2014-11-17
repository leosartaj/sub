#!/usr/bin/env python2

##
# sub
# https://github.com/leosartaj/sub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import unittest
from sub.main import get_hash
import os

class TestGetHash(unittest.TestCase):
    """
    Tests the hashing function
    """
    def setUp(self):
        """
        sets the files to work on
        """
        self.smallFile = 'smallFile.testFile'
        self.noSuchFile = '$!$!$'
        with open(self.smallFile, 'w') as f:
            f.write('Just Testing\n')
            for cou in range(5000):
                f.write(str(cou))

    def test_file_not_exists(self):
        self.assertEqual(get_hash(self.noSuchFile, 64), -1) 

    def test_get_hash_gives_hash(self):
        self.assertNotEqual(get_hash(self.smallFile, 2), -1)

    def test_fileSmall(self):
        self.assertEqual(get_hash(self.smallFile, 64), -1)

    def tearDown(self):
        os.remove(self.smallFile)

if __name__ == '__main__':
    unittest.main()
