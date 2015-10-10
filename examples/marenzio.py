#! /usr/bin/env python

from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

filename = "marenzio.mid"
top_part = NoteSeq("""
    A2 A A4 Bb2 Bb4 A2 A r4 D4'' D4. C8'' D4 Eb C2 Bb'
    D4'' C2 Bb4' A4. Bb8 C2'' C r4 D D2. C4'' Bb4' A G2 G
    A4 A8 Bb C4'' Bb' A1 G1.
    """)
middle_part = NoteSeq("""
    F#2 F# F#4 G2 G4 F#2 F# r4 Bb4 Bb4. C8'' Bb4' Bb A2 Bb
    Bb4 A2 G4 F4. G8 A2 A r4 Bb4 Bb2. A4 G F E2 E
    F4 E8 D E4 G2 F#8 E F#2 G1.
""")
bottom_part = NoteSeq("""
D2, D D4 G2,, G4 D2, D2 Bb,, Bb4., A8 G4 Eb4 F2 Bb,,
Bb4,, F2, G4 D4. Eb8 F2 F G2 G2. F4 Eb D C2 C
D4 C8 Bb, A4 G D1' G1.,
""")

# turn the volume down on the string instruments
for part in [top_part, middle_part, bottom_part]:
    for note in part:
        note.volume = 45

midi = Midi(number_tracks=3, tempo=105, instrument=48)
midi.seq_notes(top_part, track=0)
midi.seq_notes(middle_part, track=1)
midi.seq_notes(bottom_part, track=2)
midi.write(filename)
