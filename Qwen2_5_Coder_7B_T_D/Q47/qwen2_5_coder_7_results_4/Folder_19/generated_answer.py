import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:56].lower()
    for length in range(3, 8):
        pattern = re.compile('\\\\b\\\\w{' + str(length) + '}\\\\b')
        matches = pattern.findall(substring)
        for match in matches:
            if match == match[::-1]:
                result.add(match)
    return result