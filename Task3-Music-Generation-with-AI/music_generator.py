from music21 import stream, note
import random

# Create music stream
music = stream.Stream()

# Music notes
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

# Generate random notes
for i in range(20):

    random_note = random.choice(notes)

    new_note = note.Note(random_note)

    new_note.quarterLength = 1

    music.append(new_note)

# Save as MIDI file
music.write('midi', fp='generated_music.mid')

print("AI Music Generated Successfully!")