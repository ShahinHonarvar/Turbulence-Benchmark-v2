import re

def palindromes_of_specific_lengths(s):
    s = s[18:99].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 30, min(i + 51, len(s))):
            substr = s[i:j + 1]
            if substr == substr[::-1] and re.match('^[a-z]+$', substr):
                result.add(substr)
    return result