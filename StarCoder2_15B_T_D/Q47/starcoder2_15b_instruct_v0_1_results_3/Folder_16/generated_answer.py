import re

def palindromes_of_specific_lengths(string):
    substring = string[15:87]
    pattern = '[a-zA-Z]{' + str(51) + ',' + str(60) + '}'
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 51, min(i + 61, len(substring))):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes