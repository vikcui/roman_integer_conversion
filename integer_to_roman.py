# author : YANG CUI
"""
Roman numerals are represented by seven different
symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

def integer_to_roman(num):
    """
    :param num: the input integer that we are interested in converting to roman
    :return: roman form of that integer
    :time complexity: O(n) worst case but not often
    """
    romanString = ""
    while num != 0:
        if num >= 1000:
            romanString = romanString + "M"
            num = num - 1000
        elif num < 1000 and num >= 500:
            if num >= 900 and num < 1000:
                romanString = romanString + "CM"
                num = num - 900
            else:
                romanString = romanString + "D"
                num = num - 500
        elif num < 500 and num >= 100:
            if num >= 400 and num < 500:
                romanString = romanString + "CD"
                num = num - 400
            else:
                romanString = romanString + "C"
                num = num - 100
        elif num < 100 and num >= 50:
            if num >= 90 and num < 100:
                romanString = romanString + "XC"
                num = num - 90
            else:
                romanString = romanString + "L"
                num = num - 50
        elif num < 50 and num >= 10:
            if num >= 40 and num < 50:
                romanString = romanString + "XL"
                num = num - 40
            else:
                romanString = romanString + "X"
                num = num - 10
        elif num < 10 and num >= 5:
            if num >= 9 and num < 10:
                romanString = romanString + "IX"
                num = num - 9
            else:
                romanString = romanString + "V"
                num = num - 5
        elif num < 5:
            if num >= 4 and num < 5:
                romanString = romanString + "IV"
                num = num - 4
            else:
                romanString = romanString + "I"
                num = num - 1
    # print(romanString)
    return romanString

# integer_to_roman(40)