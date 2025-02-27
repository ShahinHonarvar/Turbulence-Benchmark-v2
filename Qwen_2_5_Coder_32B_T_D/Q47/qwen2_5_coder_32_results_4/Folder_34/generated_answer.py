import re

def palindromes_of_specific_lengths(s):
    s = s[200:301].lower()
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes