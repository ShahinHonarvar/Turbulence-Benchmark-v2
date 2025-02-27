import re

def palindromes_of_specific_lengths(s):
    s = s[18:99].lower()
    palindromes = set()
    for start in range(len(s) - 30):
        for end in range(start + 30, min(start + 51, len(s))):
            substring = s[start:end + 1]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes