#!/usr/bin/python3

"""
mostcharinstances(word)
returns most repeated character and number of times repeated or "no repeated characters" and 0 if there are no repeats
"""

import re

def mostcharinstances(word):
    word = str(word)
    biggest_char = ""
    biggest_char_indexes = 0
    for character in [character for character in word]:
        #uses list of character indexes in word:
        this_char_indexes = len([index.start() for index in re.finditer(character, word)])
        if (this_char_indexes > biggest_char_indexes):
                biggest_char = character
                biggest_char_indexes = this_char_indexes
    if (biggest_char_indexes < 2):
        return ["no repeated characters", 0]
    else:
        return [biggest_char, biggest_char_indexes]

#TESTS:
#for a more realistic test load, you could just read in from a CSV file to this dictionariy, just hard coded here:
#note the int 1 test value is to test in case a non-string is passed (which would never happen from a CSV test)
tests = {"fancy pants":["a",2], "123456789":["no repeated characters", 0], "":["no repeated characters", 0], 1:["no repeated characters", 0], 12341:["1",2], 1123411:["1",4], 1243441:["4",3]}

for word, character_number in tests.items():
    print("test word: \"" + str(word) + "\", correct return value: \"" + str(character_number) + "\", test result: \"" + str(mostcharinstances(word)) +"\"")
