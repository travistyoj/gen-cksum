#!/usr/bin/python
# Written by TravistyOJ

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