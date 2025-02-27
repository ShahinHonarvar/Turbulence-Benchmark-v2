import re

def palindromes_of_specific_lengths(s):
    s = s[11:94].lower()
    result = set()
    for i in range(len(s) - 33):
        for j in range(i + 34, min(i + 55, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result