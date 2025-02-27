import re

def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    palindromes = set()
    for i in range(len(s) - 41):
        for j in range(i + 41, min(i + 78, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes