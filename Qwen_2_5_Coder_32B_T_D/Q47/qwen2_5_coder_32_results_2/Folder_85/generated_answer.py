import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[29:99].lower()
    for i in range(len(s) - 5):
        for j in range(i + 5, min(i + 10, len(s))):
            substr = s[i:j + 1]
            if re.fullmatch('[a-z]+', substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes