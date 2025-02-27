import re

def palindromes_of_specific_lengths(s):
    s = s[10:76].lower()
    palindromes = set()
    for i in range(len(s) - 9):
        for j in range(i + 10, min(i + 21, len(s)) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and re.fullmatch('[a-z]+', substr):
                palindromes.add(substr)
    return palindromes