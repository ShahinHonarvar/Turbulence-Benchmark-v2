import re

def palindromes_of_specific_lengths(s):
    s = s[75:96].lower()
    palindromes = set()
    for i in range(len(s) - 6):
        for j in range(i + 7, min(i + 10, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes