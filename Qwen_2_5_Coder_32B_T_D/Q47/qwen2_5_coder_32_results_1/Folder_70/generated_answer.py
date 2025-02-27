import re

def palindromes_of_specific_lengths(s):
    s = s[10:71].lower()
    palindromes = set()
    for i in range(len(s) - 23):
        for j in range(i + 24, min(i + 53, len(s)) + 1):
            substring = re.sub('[^a-z]', '', s[i:j])
            if substring == substring[::-1] and 24 <= len(substring) <= 52:
                palindromes.add(substring)
    return palindromes