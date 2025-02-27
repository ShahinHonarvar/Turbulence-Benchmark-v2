import re

def palindromes_of_specific_lengths(s):
    s = s[31:92].lower()
    palindromes = set()
    for start in range(len(s) - 49):
        for length in range(50, 54):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes