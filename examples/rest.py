#!/usr/bin/env python

from pyknon.genmidi import Midi
from pyknon.music import Note, Rest, NoteSeq

filename = "rest.mid"
midi = Midi(1, tempo=120)
midi.seq_notes(NoteSeq("r1"))
midi.write(filename)
print "wrote ", filename
