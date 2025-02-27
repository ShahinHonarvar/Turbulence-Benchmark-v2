import re

def palindromes_of_specific_lengths(s):
    substring = s[1:300]
    result = set()
    for i in range(3, min(11, len(substring) + 1)):
        for j in range(len(substring) - i + 1):
            candidate = substring[j:j + i]
            if re.fullmatch('[a-zA-Z]+', candidate) and candidate.lower() == candidate[::-1].lower():
                result.add(candidate)
    return result