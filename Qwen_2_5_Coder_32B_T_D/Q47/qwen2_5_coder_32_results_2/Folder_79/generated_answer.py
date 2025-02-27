import re

def palindromes_of_specific_lengths(s):
    s = s[1:9].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, min(i + 5, len(s)) + 1):
            w = s[i:j]
            if re.match('^[a-z]+$', w) and w == w[::-1]:
                palindromes.add(w)
    return palindromes