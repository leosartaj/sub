#!/usr/bin/env python2

##
# sub
# https://github.com/leosartaj/sub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from hashlib import md5
import requests 
import os, optparse, socket

def parse_args():
    usage = """usage: %prog [options] [path]

    Run 
    sub -h/--help
    For help
"""

    parser = optparse.OptionParser(usage)

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

def pDir():
    """
    gives the present working directory
    """
    return os.getcwd()

def fileExists(fName, dire=pDir()):
    """
    Check if a file exists
    """
    if os.path.isfile(os.path.join(dire, fName)):
        return True
    return False

def dirExists(dire):
    """
    Check if a directory exists
    """
    if os.path.isdir(dire):
        return True
    return False

def get_hash(fName, readSize, dire=pDir()):
    """
    creates the required hash
    """
    if not fileExists(fName, dire):
        return -1
    readSize = readSize * 1024 # bytes to be read
    fName = os.path.join(dire, fName) # name coupled with path
    with open(fName, 'rb') as f:
        size = os.path.getsize(fName)
        if size < readSize * 2:
            return -1
        data = f.read(readSize)
        f.seek(-readSize, os.SEEK_END)
        data += f.read(readSize)
    return md5(data).hexdigest() # return md5 hash

def download_file(fName, time, dire=pDir()):
    """
    download the required subtitle
    """
    # hash
    gen_hash = get_hash(fName, 64, dire)
    if gen_hash == -1:
        return -1

    # making request
    user_agent = {'User-agent': 'SubDB/1.0 (sub/0.1; http://github.com/leosartaj/sub)'}
    param = {'action': 'download', 'hash': gen_hash, 'language': 'en'} # Specification for the request
    try:
        r = requests.get("http://api.thesubdb.com/", headers = user_agent, params = param, timeout=time) # Get Request
    except (requests.exceptions.Timeout, socket.error):
        return 'Timeout Error'
    if r.status_code != 200:
        return r.status_code

    # save file
    fName, fExt = os.path.splitext(fName)
    fName += '.srt' # replace extension with srt
    fName = os.path.join(dire, fName) # name coupled with path
    with open(fName, 'wb') as f:
        f.write(r.text.encode('ascii', 'ignore'))

    return r.status_code

def file_downloaded(dwn, fName, verbose=False):
    """
    print for downloaded file
    """
    if verbose:
        if dwn == 200:
            fName, fExt = os.path.splitext(fName)
            print 'Downloaded ' + fName + '.srt'
            return True
        elif dwn != -1:
            print 'Tried downloading got ' + str(dwn) + ' for ' + fName
            return False

def download(name, options):
    """
    download a file or all files in a directory
    """
    dire = os.path.dirname(name) # returns the directory name
    fName = os.path.basename(name) # returns the filename
    fNameOnly, fExt = os.path.splitext(fName)

    dwn = 0

    if fileExists(fName, dire) and not fileExists((fNameOnly + '.srt'), dire): # skip if already downloaded
        if file_downloaded(download_file(fName, options.timeout, dire), fName, options.verbose):
            dwn += 1
    elif dirExists(name):
        for filename in os.listdir(name):
            if options.recursive:
                dwn += download(os.path.join(name, filename), options)
            else:
                if file_downloaded(download_file(filename, options.timeout, name), filename, options.verbose):
                    dwn += 1
    return dwn
