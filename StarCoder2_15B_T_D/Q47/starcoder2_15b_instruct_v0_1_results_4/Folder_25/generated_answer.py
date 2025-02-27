import re

def palindromes_of_specific_lengths(s):
    substring = s[26:85]
    pattern = '[a-zA-Z]{' + str(30) + ',' + str(46) + '}'
    palindromes = set()
    for length in range(30, 47):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes