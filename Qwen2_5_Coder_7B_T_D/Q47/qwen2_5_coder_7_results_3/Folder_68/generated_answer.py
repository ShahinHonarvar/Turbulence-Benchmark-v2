import re

def palindromes_of_specific_lengths(s):
    s = s[:51].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 50, min(len(s), i + 101)):
            substring = s[i:j]
            if re.fullmatch('[a-z]{50,100}', substring) and substring == substring[::-1]:
                result.add(substring)
    return result