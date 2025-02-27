import re

def palindromes_of_specific_lengths(s):
    result = set()
    s = s[65:100].lower()
    for i in range(len(s) - 25):
        for j in range(i + 25, min(i + 34, len(s))):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result