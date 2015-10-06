
# Example representations of musical structures
# NOT Pyknon code

class RhythmSeq:
    '''A sequence of rhythmic durations'''
    # implementation here
    pass

# "r" represents a rest
RhythmSeq("4 4 4 4") # four quarter notes
RhythmSeq("4 4 8 8 4")

RhythmSeq("4 8 8 4 4")
RhythmSeq("r4 4 4 r4")








###################################
###################################
###################################

class NoteSeq:
    '''A sequence of notes with rhythms'''
    # implementation here
    pass

# letter-name + rhythm
NoteSeq("C4 D4 E4 D4 C2")
# can include rests
NoteSeq("C4 r4 E4 D4 C2")
# same duration is applied until changed
NoteSeq("C4 r E D2 C") == NoteSeq("C4 r4 E4 D2 C2")








####################################################
####################################################
####################################################

# name/value + rhythm + octave
NoteSeq("C2 C4, C C1'")

# same octave and duration applied until changed
NoteSeq("C#4' D8 E A4 C#'")









###################################################
###################################################
###################################################
