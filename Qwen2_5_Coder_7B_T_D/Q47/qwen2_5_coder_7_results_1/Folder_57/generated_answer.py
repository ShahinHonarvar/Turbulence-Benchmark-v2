import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:95].lower()
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.fullmatch('[a-z]+', candidate) and candidate == candidate[::-1]:
                result.add(candidate)
    return result