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
    try:
        download(sys.argv[1])
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()

