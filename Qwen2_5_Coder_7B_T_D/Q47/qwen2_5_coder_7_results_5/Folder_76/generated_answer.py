import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[101:293].lower()
    pattern = re.compile('[a-zA-Z]{154,182}')
    matches = pattern.findall(substring)
    for match in matches:
        if match == match[::-1]:
            result.add(match)
    return result