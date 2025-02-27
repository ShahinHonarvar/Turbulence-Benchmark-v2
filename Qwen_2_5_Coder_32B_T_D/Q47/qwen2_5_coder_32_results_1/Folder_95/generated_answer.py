import re

def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    palindromes = set()
    for i in range(len(s) - 19):
        for length in (20, 21):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes