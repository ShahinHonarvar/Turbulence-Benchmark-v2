import re

def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    s = re.sub('[^a-z]', '', s)
    result = set()
    for start in range(len(s) - 2):
        for end in range(start + 2, min(start + 6, len(s)) + 1):
            substring = s[start:end]
            if substring == substring[::-1]:
                result.add(substring)
    return result