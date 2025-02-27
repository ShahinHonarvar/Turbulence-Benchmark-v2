import re

def palindromes_of_specific_lengths(s):
    s = s[11:94].upper()
    palindromes = set()
    for start in range(len(s) - 33):
        for length in range(34, 55):
            if start + length <= len(s):
                substring = s[start:start + length]
                if re.match('^[A-Z]+$', substring) and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes