#!/usr/bin/python
# Written by TravistyOJ
# A portable Python script to calculate and fix the checksum of a given SEGA
# Genesis/Mega Drive ROM file.
#
# MIT License
#
# Copyright (c) 2016 Travis Brown
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys, struct

if len(sys.argv) != 2:
	print "Usage: %s <filename>" % sys.argv[0]
else:
	with open(sys.argv[1], 'r+b') as rom:
		rom.seek(0x18E)
		curr_cksum = struct.unpack('>H', rom.read(2))[0]
		rom.seek(0x200)
		calc_cksum = 0
		while True:
			word = rom.read(2)
			if not word: break
			calc_cksum += struct.unpack('>H', word)[0]
		calc_cksum &= 0xffff
		print "Found checksum: %s" % hex(curr_cksum)
		print "Calcd checksum: %s" % hex(calc_cksum)
		if curr_cksum == calc_cksum:
			print "Checksum correct!"
		else:
			rom.seek(0x18E)
			rom.write(struct.pack('>H', calc_cksum))
			print "Checksum fixed!"
