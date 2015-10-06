#!/usr/bin/env python

from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq

filename = "key_of_A.mid"
notes1 = NoteSeq("C#4' D8 E A4 C#")

midi = Midi(1, tempo=90)
midi.seq_notes(notes1, track=0)
midi.write(filename)
print "wrote ", filename
