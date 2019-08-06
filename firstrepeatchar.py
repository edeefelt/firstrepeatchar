#!/usr/bin/python3

"""
firstrepeatchar(word)
returns first repeat character reading left to right or null string "" if no repeat character is found
"""

import re

def firstrepeatchar(word):
    word = str(word)
    for character in [character for character in word]:
        #uses list of character indexes in word:
        if (len([index.start() for index in re.finditer(character, word)]) > 1):
                return character
    return ""

#TESTS:
#for a more realistic test load, you could just read in from a CSV file to a dictionariy, just hard coded here:
tests = {"fancy pants":"a", "123456789":"", "":"", 1:"", 12341:"1"} #note the int 1 test value is to test in case a non-string is passed (which would never happen from a CSV test)

for word, character in tests.items():
    print("test word: \"" + str(word) + "\", correct return value: \"" + character + "\", test result: \"" + firstrepeatchar(word) +"\"")
