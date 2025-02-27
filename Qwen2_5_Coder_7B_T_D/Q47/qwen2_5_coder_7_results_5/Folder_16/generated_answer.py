import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[15:87]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 51, min(i + 61, len(substring) + 1)):
            sub = substring[i:j]
            if sub == sub[::-1] and re.match('^[a-z]+$', sub):
                palindromes.add(sub)
    return palindromes