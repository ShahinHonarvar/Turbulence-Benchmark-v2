import re

def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    s = re.sub('[^a-z]', '', s)
    result = set()
    for length in range(40, 48):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result