#! /usr/bin/env python

from __future__ import division
from pyknon.genmidi import Midi
from pyknon.music import Rest, Note, NoteSeq

filename
top_part = NoteSeq("A2 A A4 Bb2 Bb4 A2 A r4 D4'") + NoteSeq([Note(value=2,octave=6,dur=3/8)]) + NoteSeq("C8 D4 Eb C2 Bb, D4' C2 Bb4,") + NoteSeq([Note(value=9,octave=5,dur=3/8)]) + NoteSeq("Bb8 C2' C r4 D") + NoteSeq([Note(value=2, octave=6, dur=3/4)]) + NoteSeq("C4 Bb4, A G2 G") + NoteSeq("A4 A8 Bb C4' Bb, A1 G1")
middle_part = NoteSeq("")
bottom_part = NoteSeq("")
midi = Midi(num_tracks=3, tempo=120)
midi.seq_notes(top_part)
midi.write("marenzio.mid")
