import re

def palindromes_of_specific_lengths(s):
    s = s[15:95].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 18, min(i + 74, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and re.match('^[a-z]+$', substr):
                result.add(substr)
    return result