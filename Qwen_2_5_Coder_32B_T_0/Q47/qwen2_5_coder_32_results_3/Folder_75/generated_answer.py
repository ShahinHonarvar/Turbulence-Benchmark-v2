import re

def palindromes_of_specific_lengths(s):
    s = s[31:75].lower()
    palindromes = set()
    for i in range(len(s) - 22):
        for j in range(i + 23, min(i + 40, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes