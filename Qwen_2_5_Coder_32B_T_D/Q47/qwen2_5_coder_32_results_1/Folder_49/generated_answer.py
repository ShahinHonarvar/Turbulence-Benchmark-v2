import re

def palindromes_of_specific_lengths(s):
    s = s[10:101].lower()
    palindromes = set()
    for i in range(len(s) - 9):
        for j in range(i + 10, min(i + 51, len(s) + 1)):
            substring = s[i:j]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes