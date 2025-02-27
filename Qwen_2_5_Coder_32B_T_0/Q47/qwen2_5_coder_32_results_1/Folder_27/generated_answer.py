import re

def palindromes_of_specific_lengths(s):
    s = s[13:100].lower()
    palindromes = set()
    for i in range(len(s) - 25):
        for j in range(i + 25, min(i + 30, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes