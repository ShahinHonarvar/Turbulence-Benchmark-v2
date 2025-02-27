import re

def palindromes_of_specific_lengths(s):
    s = s[:101].lower()
    r = re.compile('[a-z]{3,15}')
    palindromes = set()
    for match in r.finditer(s):
        w = match.group()
        if w == w[::-1]:
            palindromes.add(w)
    return palindromes