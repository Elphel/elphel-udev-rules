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
@contact:    andrey@elphel.com
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

def create_udev_rules_file(contents):
  c  = "# --- This is an auto-generated file, see "+sys.argv[0]+"\n"
  c += "ACTION!=\"add\", GOTO=\"static_nodes_end\"\n\n"
  c += contents
  c += "\nLABEL=\"static_nodes_end\""

  f = open('50-elphel-static-nodes.rules','w')
  f.write(c)
  f.close()

def get_udev_rule(mode, name, devtype, major, minor,comment):
  tmpstr  = comment.strip()+"\n"
  tmpstr += "ACTION==\"add\", RUN+=\"/bin/mknod -m "+mode+" /dev/"+name+" "+devtype+" "+major+" "+minor+"\"\n"
  return tmpstr

def process_header():

    rulestr = ""

    print("# --- This is an auto-generated file, see %s ---"%(sys.argv[0]))
    print("define mknodes =")
    pat=re.compile(r'#define\s+(\w+)\s+\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*,\s*(\w*)\s*,\s*(\w*)\s*,\s*"([^"]+)"\s*,\s*"([^"]+)"\s*\)(.*)')
    """ Example of a string to match:
    #define DEV393_I2C_ENABLE     ("xi2cenable",        "fpga_xi2c",     134,  7, "0666", "c")  ///< enable(/protect)...
    groups:       1                     2                   3             4    5     6     7            8
    """
    f = open(sys.argv[1], "r")
    line = f.readline()
    while line:
        fs = pat.search(line)
        if fs:
            comment = fs.group(8).strip(" \t/<*")
            if comment:
                comment = " # "+comment
            print("mknod -m %s $(TARGETDIR)/%-20s %s %3s %3s%s"%(
                fs.group(6), fs.group(2), fs.group(7), fs.group(4), fs.group(5), comment))

            rulestr += get_udev_rule(fs.group(6), fs.group(2), fs.group(7), fs.group(4), fs.group(5), comment)

        line = f.readline()

    if rulestr != "":
        create_udev_rules_file(rulestr)

    print("endef")
if __name__ == "__main__":
    process_header()
