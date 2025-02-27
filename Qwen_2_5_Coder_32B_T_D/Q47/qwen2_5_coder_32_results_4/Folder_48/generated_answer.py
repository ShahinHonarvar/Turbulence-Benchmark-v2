import re

def palindromes_of_specific_lengths(s):
    s = s[155:284].lower()
    result = set()
    for length in range(104, 121):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                result.add(substring)
    return result