import re

def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    result = set()
    for length in range(40, 48):
        pattern = '\\\\b\\\\w{' + str(length) + '}\\\\b'
        for match in re.finditer(pattern, s):
            result.add(match.group())
    return result