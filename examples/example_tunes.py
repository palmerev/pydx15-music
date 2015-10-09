#!/usr/bin/env python

from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq

notes1 = NoteSeq("D4' F#8 A D4")
midi = Midi(1, tempo=90)
midi.seq_notes(notes1, track=0)
midi.write("octave_test2.mid")

####################################

# a melody from Star Wars
sw = NoteSeq(
    "D2, A G16 F#16 E8 D2' A4, G16 F#16 E8 D2' A4, G16 F#16 G8 E1"
    )
sw_midi = Midi(1, tempo=120)
sw_midi.seq_notes(sw, track=0)
sw_midi.write("sw.mid")

####################################

# Beethoven's "Ode to Joy" theme, one track
filename = "beethoven_one_track.mid"
bn_part_a = NoteSeq(
    "B4 B C'' D D C B' A G G A B B A A2 B4 B C'' D D C B, A G G A B A G G"
    )
bn_part_b = NoteSeq("A4 A B G A B8 C'' B4 G A B8 C'' B4 A G A D")

bn_midi = Midi(1, tempo=120)
bn_midi.seq_notes(bn_part_a + bn_part_b, track=0)
bn_midi.write(filename)

# "Ode to Joy", test adding a second track
#
###########################################

# "Frere Jacques", a round in two tracks
filename = "frere-jacques-two-track.mid"
fj_notes1 = NoteSeq("C4' D E C C D E C E F G2 E4 F G2")
fj_notes2 = NoteSeq(
    "G8 A G F E4 C G8 A G F E4 C C G, C2' C4 G, C2'"
    )
all_notes = fj_notes1 + fj_notes2

fj_midi = Midi(2, tempo=120)
fj_midi.seq_notes(all_notes, track=0)
fj_midi.seq_notes(all_notes, track=1, time=8)
fj_midi.write(filename)



##########################################
