import re

def palindromes_of_specific_lengths(s):
    s = s[13:100].lower()
    palindromes = set()
    for start in range(len(s) - 25):
        for length in range(26, 30):
            if start + length <= len(s):
                substring = s[start:start + length]
                if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes