import re

def palindromes_of_specific_lengths(s):
    result = set()
    s = s[41:90].lower()
    for i in range(len(s) - 23 + 1):
        for j in range(i + 23, min(i + 39, len(s) + 1)):
            substr = s[i:j]
            if re.fullmatch('[a-z]+', substr) and substr == substr[::-1]:
                result.add(substr)
    return result