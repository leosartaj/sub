#! /bin/sh

##
# PySub
# https://github.com/leosartaj/PySub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# The directory where the install.sh script is kept
SCRIPT_DIR=$(readlink -f ${0%/*})

# Install files
install -m 0755 "$SCRIPT_DIR"/PySub/pysub.py /usr/bin/pysub
