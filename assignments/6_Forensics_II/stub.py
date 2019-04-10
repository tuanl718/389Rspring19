#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
timestamp = struct.unpack("<L", data[8:12])[0]
author = struct.unpack("<8s", data[12:20])[0]
sectioncount = struct.unpack("<L", data[20:24])[0]

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

if (timestamp < 0 or timestamp > 2147483647):
    bork("Bad timestamp! Got %d, not between 0 and 2147483647" % int(timestamp))

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

if is_ascii(str(author)) == False:
    bork("Bad author! Got %s, not ASCII-encoded" % str(author))

if sectioncount <= 0:
    bork("Bad section couunt! Got %d, but must be greater than 0" % int(sectioncount))

ts = int(timestamp)
newtimestamp = (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % newtimestamp)
print("AUTHOR: %s" % str(author))
print("SECTION COUNT: %d" % int(sectioncount))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

SECTION_ASCII = 0x1
SECTION_UTF = 0x2
SECTION_WORDS = 0x3
SECTION_DWORDS = 0x4
SECTION_DOUBLES = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_PNG = 0x8
SECTION_GIF87 = 0x9
SECTION_GIF89 = 0xA

print("-------  BODY  -------")

offset = 24
count = 0

#while count < str(sectioncount):
#    
#    stype, slen = struct.unpack_from("<LL", data, offset)
#    offset = offset + 8
#
#    if stype = SECTION_ASCII:
#        output = struct.unpack_from("<%ds," % %slen, data, offset)
#
    



