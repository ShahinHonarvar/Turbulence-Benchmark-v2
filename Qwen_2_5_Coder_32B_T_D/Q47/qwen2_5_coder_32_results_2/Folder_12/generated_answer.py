import re

def palindromes_of_specific_lengths(s):
    s = s[62:89].lower()
    palindromes = set()
    for i in range(len(s) - 17):
        for j in range(i + 18, i + 22):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes