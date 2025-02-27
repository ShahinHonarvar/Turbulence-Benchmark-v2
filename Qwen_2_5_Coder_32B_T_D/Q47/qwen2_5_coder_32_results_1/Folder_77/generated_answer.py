import re

def palindromes_of_specific_lengths(s):
    s = s[103:277].lower()
    result = set()
    for start in range(len(s)):
        for end in range(start + 99, min(start + 170, len(s))):
            substring = s[start:end + 1]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                result.add(substring)
    return result