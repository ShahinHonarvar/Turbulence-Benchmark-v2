import re

def palindromes_of_specific_lengths(s):
    s = s[24:98].lower()
    palindromes = set()
    for i in range(len(s) - 9):
        for j in range(i + 10, min(i + 37, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes