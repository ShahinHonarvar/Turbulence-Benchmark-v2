import re

def palindromes_of_specific_lengths(s):
    s = s[32:72].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for start in range(len(s) - 20):
        for end in range(start + 20, min(start + 32, len(s)) + 1):
            substring = s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes