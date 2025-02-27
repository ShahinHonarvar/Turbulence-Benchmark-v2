import re

def palindromes_of_specific_lengths(s):
    s = s[28:95].lower()
    palindromes = set()
    for i in range(len(s) - 37):
        for j in range(i + 38, min(i + 50, len(s) + 1)):
            substring = s[i:j]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes