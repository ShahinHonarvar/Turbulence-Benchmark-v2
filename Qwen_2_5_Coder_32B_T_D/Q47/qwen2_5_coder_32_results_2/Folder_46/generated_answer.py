import re

def palindromes_of_specific_lengths(s):
    s = s[11:98].lower()
    palindromes = set()
    for start in range(len(s) - 28):
        for length in range(29, 63):
            substring = s[start:start + length]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes