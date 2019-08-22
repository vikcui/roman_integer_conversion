# author: YANG CUI
"""
This program converts roman letters to integers.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""
def mapRomanLetters(inputLetter):
    # time complexity: O(1)
    if inputLetter == "I":
        return 1
    elif inputLetter == "V":
        return 5
    elif inputLetter == "X":
        return 10
    elif inputLetter == "L":
        return 50
    elif inputLetter == "C":
        return 100
    elif inputLetter == "D":
        return 500
    elif inputLetter == "M":
        return 1000

def roman_to_integer(inputString):
    # time complexity: O(n)
    # compute the length of the input string
    stringLen = len(inputString)
    # integer result accumulator
    integerResult = 0
    position = 0
    # basic loop structure to translate roman letters to integers:
    while position < stringLen:
        # look ahead position
        nextPos = position + 1
        if nextPos <= stringLen - 1:
            if mapRomanLetters(inputString[nextPos]) > mapRomanLetters(inputString[position]):
                integerResult = integerResult + mapRomanLetters(inputString[nextPos]) - mapRomanLetters(inputString[position])
                position = position + 1
            else:
                integerResult = integerResult + mapRomanLetters(inputString[position])
        else:
            integerResult = integerResult + mapRomanLetters(inputString[position])
        position = position + 1
    # print(integerResult)
    return integerResult
# roman_to_integer("MCMXCIV")



