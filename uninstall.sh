#! /bin/sh

##
# PySub
# https://github.com/leosartaj/PySub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

path=/usr/bin/pysub

if [ -f "$path" ]
then
    rm -f "$path"
else
    echo 'PySub is not installed yet. Use install.sh to install.'
fi
