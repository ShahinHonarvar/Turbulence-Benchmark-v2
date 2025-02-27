import re

def palindromes_of_specific_lengths(s):
    s = s[17:96].lower()
    r = re.compile('[a-z]')
    palindromes = set()
    for i in range(len(s) - 12):
        for j in range(i + 12, min(i + 49, len(s))):
            if s[i:j + 1] == s[i:j + 1][::-1] and all((r.match(c) for c in s[i:j + 1])):
                palindromes.add(s[i:j + 1])
    return palindromes