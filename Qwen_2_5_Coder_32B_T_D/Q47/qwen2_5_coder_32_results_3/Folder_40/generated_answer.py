import re

def palindromes_of_specific_lengths(s):
    s = s[:6].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, min(i + 6, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes