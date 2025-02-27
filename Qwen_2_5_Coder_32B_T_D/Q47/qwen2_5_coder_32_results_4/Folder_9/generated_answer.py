import re

def palindromes_of_specific_lengths(s):
    s = s[:301]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    for start in range(len(s) - 49):
        for end in range(start + 49, min(start + 60, len(s))):
            substring = s[start:end + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes