#!/usr/bin/python2

##
# PySub
# https://github.com/leosartaj/PySub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from api import download
import sys

def main():
    if len(sys.argv) == 3: 
        download(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        download(sys.argv[1])

if __name__ == '__main__':
    main()

