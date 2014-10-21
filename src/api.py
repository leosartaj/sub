#!/usr/bin/env python2

##
# PySub
# https://github.com/leosartaj/PySub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from hashlib import md5
import requests 
import os

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
#print get_hash('blacklists02e05.mp4', 64, '/home/leosartaj/Downloads/')

def download_file(fName, dire=pDir()):
    """
    download the required subtitle
    """
    # hash
    gen_hash = get_hash(fName, 64, dire)
    if gen_hash == -1:
        return -1

    # making request
    user_agent = {'User-agent': 'SubDB/1.0 (PySub/0.1; http://github.com/leosartaj/PySub)'}
    param = {'action': 'download', 'hash': gen_hash, 'language': 'en'} # Specification for the request
    r = requests.get("http://api.thesubdb.com/", headers = user_agent, params = param) # Get Request
    if r.status_code != 200:
        return r.status_code

    # save file
    fName += '.srt'
    fName = os.path.join(dire, fName) # name coupled with path
    with open(fName, 'wb') as f:
        f.write(r.text.encode('ascii', 'ignore'))

    return r.status_code
#print download_file('blacklists02e05.mp4', '/home/leosartaj/Downloads')

def file_downloaded(fName):
    """
    print the name of file 
    """
    print 'Downloaded ' + fName + '.srt'

def download(dire=pDir(), fName=None):
    """
    download a file or all files in a directory
    """
    downloaded = 0

    if fName == None:
        for filename in os.listdir(dire):
            if download_file(filename, dire) == 200:
                file_downloaded(filename)
                downloaded += 1
    else:
        if download_file(fName, dire) == 200:
            file_downloaded(fName)
            downloaded += 1

    return downloaded
#print download('/home/leosartaj/Downloads/tbbts08e04')
#print download('/home/leosartaj/Downloads', 'blacklists02e05.mp4')
