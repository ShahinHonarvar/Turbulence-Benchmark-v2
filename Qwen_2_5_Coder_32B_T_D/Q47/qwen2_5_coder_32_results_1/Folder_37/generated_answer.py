import re

def palindromes_of_specific_lengths(s):
    s = s[:10].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, min(i + 6, len(s)) + 1):
            substr = re.sub('[^a-z]', '', s[i:j])
            if substr == substr[::-1] and substr:
                palindromes.add(substr)
    return palindromes