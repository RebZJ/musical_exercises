from random import *

#number of intervals and distance from unison
dict_intervals = {0:'unison', 1:'minor 2nd', 2:'major 2nd', 3:'minor 3rd', 4:'major 3rd', 5:'perfect 4th', 6:'tritone', 7:'perfect 5th', 8:'minor 6th', 9:'major 6th', 10:'minor 7th', 11:'major 7th', 12:'octave'}

#direction of movement
direction = ['up', 'down']

#key signatures 0 being A and A#/Bb being 1 etc. each 12 keys assigned 0-11
key_sig = {0:'A', 2:'B', 3:'C', 5:'D', 7:'E', 8:'F', 10:'G'}

#accidentals
accidental = ['', '#', 'b']

#
list_chords = ['maj', 'min', 'dim', 'min7', 'maj7', 'mMaj7', 'm7b5']

#generates a bunch of intervals for me to practice
def do_intervals(num, action):
	for x in range(num):

		interval = choice(list(dict_intervals.values()))
		current_key = '0'

		if (interval == 'unison'):
			print("%s in unison a %s%s" %(action,choice(list(key_sig.values())),choice(accidental)))

		else:
			print("%s a %s %s from %s%s" %(action, interval, choice(direction), choice(list(key_sig.values())), choice(accidental))) 
	
	print("\n")
#notes in a given chord, randomly generates a chord from the given chord list above
def chord_notes(num):
	for x in range(num):
		print("what are the notes in the chords %s%s %s?" %(choice(list(key_sig.values())), choice(accidental),choice(list_chords)))
	
	print("\n")
