import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(38, 61):
        for i in range(18, 88 - length + 1):
            substring = s[i:i + length]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                result.add(substring)
    return result