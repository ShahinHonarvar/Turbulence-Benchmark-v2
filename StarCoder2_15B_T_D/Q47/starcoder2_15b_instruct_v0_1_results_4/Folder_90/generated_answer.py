import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(136) + ',' + str(151) + '}'
    substring = string[106:281]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes