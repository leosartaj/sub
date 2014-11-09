#!/usr/bin/env python2

##
# sub
# https://github.com/leosartaj/sub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import unittest
from sub.sub import download_file
import os

class TestDownloadFile(unittest.TestCase):
    """
    Tests the hashing function
    """
    def setUp(self):
        """
        sets the files to work on
        """
        self.smallFile = 'smallFile.testFile'
        self.largeFile = 'largeFile.testFile'
        self.noSuchFile = '$!$!$'

        with open(self.smallFile, 'w') as f:
            f.write('Just Testing 1\n')

        with open(self.largeFile, 'w') as f:
            f.write('Just Testing 2\n')
            for cou in range(100000):
                f.write(str(cou))

    def test_file_not_exists(self):
        self.assertEqual(download_file(self.noSuchFile), -1) 

    def test_fileSmall(self):
        self.assertEqual(download_file(self.smallFile), -1)

    def test_largeFile(self):
        """
        test for a large file (404 expected)
        cannot test for an actual media file
        because that will be heavy
        Nobody downloads such heavy code for such a small script
        """
        self.assertEqual(download_file(self.largeFile), 404) # if all goes well file will not be found

    def tearDown(self):
        os.remove(self.smallFile)
        os.remove(self.largeFile)

if __name__ == '__main__':
    unittest.main()

