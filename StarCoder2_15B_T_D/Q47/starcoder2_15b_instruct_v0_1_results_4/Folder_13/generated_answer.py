import re

def palindromes_of_specific_lengths(string):
    substring = string[13:96]
    pattern = '[a-zA-Z]{' + str(57) + ',' + str(60) + '}'
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 57, i + 61):
            window = substring[i:j]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes