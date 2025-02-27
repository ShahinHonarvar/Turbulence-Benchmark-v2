import re

def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    palindromes = set()
    for i in range(len(s) - 19):
        for j in range(20, 22):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes