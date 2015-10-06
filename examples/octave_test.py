#!/usr/bin/env python

from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq

filename = "scale_octaves.mid"
notes1 = NoteSeq(
    "C4 D E F G A B C4'' B' A G F E D C B, C' A G F E D C"
    )
midi = Midi(1, tempo=90)
midi.seq_notes(notes1, track=0)
midi.write(filename)
print("wrote ", filename)
