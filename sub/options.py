#!/usr/bin/env python2

##
# sub
# https://github.com/leosartaj/sub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import optparse
import os

try:
    from sub import __desc__ # try for version number
except ImportError:
    __desc__ = 'UNKNOWN'

def parse_args():
    usage = """usage: %prog [options] [path]

    Run 
    sub -h/--help
    For help
"""

    parser = optparse.OptionParser(usage, version=__desc__)

    help = "For verbose output"
    parser.add_option('--verbose', '-v', action='store_true', help=help, dest='verbose')

    help = "For recursive subtitle downloading"
    parser.add_option('--recursive', '-r',  action='store_true', help=help, dest='recursive')

    help = "Set Timeout for download"
    parser.add_option('--timeout', '-t', type='float',  help=help, default=30)

    options, args = parser.parse_args()

    if len(args) == 0:
        parser.error('Not enough arguments')

    dwn_this = []
    for arg in args:
        if not os.path.exists(arg):
            parser.error('No such file/dir: %s' % arg)
        dwn_this.append(arg)

    return options, dwn_this
