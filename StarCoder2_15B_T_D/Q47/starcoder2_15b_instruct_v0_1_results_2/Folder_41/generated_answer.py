import re

def palindromes_of_specific_lengths(s):
    s_lower = s.lower()
    substring = s_lower[1:8]
    pattern = '[a-z]{' + str(3) + ',' + str(4) + '}'
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 5, len(substring) + 1)):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes