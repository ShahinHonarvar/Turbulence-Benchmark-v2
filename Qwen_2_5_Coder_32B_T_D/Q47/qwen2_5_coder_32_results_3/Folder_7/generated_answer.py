import re

def palindromes_of_specific_lengths(s):
    s = s[119:257].lower()
    result = set()
    for length in range(104, 124):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if re.fullmatch('[a-z]*', substring) and substring == substring[::-1]:
                result.add(substring)
    return result