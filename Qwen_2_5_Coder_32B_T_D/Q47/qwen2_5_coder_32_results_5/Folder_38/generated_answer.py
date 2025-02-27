import re

def palindromes_of_specific_lengths(s):
    s = s[18:88].lower()
    result = set()
    for start in range(len(s) - 37):
        for end in range(start + 38, min(start + 61, len(s)) + 1):
            substring = s[start:end]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                result.add(substring)
    return result