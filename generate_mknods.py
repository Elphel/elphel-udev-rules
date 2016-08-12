#!/usr/bin/env python
# encoding: utf-8
'''
# Copyright (C) 2016, Elphel.inc.
# Generate static device nodes from the header file with drivers/devices definitions
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

@author:     Andrey Filippov
@copyright:  2016 Elphel, Inc.
@license:    GPLv3.0+
@contact:    andrey@elphel.coml
@deffield    updated: Updated
'''
from __future__ import division
from __future__ import print_function
#from __builtin__ import str
import sys
import re
__author__ = "Andrey Filippov"
__copyright__ = "Copyright 2015, Elphel, Inc."
__license__ = "GPL"
__version__ = "3.0+"
__maintainer__ = "Andrey Filippov"
__email__ = "andrey@elphel.com"
__status__ = "Development"
def process_header():
    print("define mknodes =")
#    files = []
    pat=re.compile(r'#define\s+(\w+)\s+\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*,\s*(\w*)\s*,\s*(\w*)\s*,\s*"([^"]+)"\s*,\s*"([^"]+)"\s*\)(.*)')
    f = open(sys.argv[1], "r")
    line = f.readline()
    while line:
        fs = pat.search(line)
        if fs:
            print("mknod -m %s $(TARGETDIR)/%-20s %s %3s %3s #%s"%(
                fs.group(6), fs.group(2), fs.group(7), fs.group(4), fs.group(5), fs.group(8).strip(" \t/<*")))
#            files.append(fs.group(2))
        line = f.readline()
#    for f in files:
#        print("chown root:root $(TARGETDIR)/%-20s"%(f))
    print("endef")
#    mknod -m 0622   $(TARGETDIR)/circbuf0   c 135   32
if __name__ == "__main__":
    process_header()
