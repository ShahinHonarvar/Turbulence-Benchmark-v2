import re

def palindromes_of_specific_lengths(s):
    s = s[15:90].lower()
    palindromes = set()
    for i in range(len(s) - 39):
        for j in range(i + 40, min(i + 73, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes