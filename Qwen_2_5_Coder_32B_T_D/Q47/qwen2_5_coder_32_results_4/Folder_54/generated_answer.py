import re

def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    palindromes = set()
    for i in range(len(s) - 17):
        for j in range(18, 20):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                    palindromes.add(substring)
    return palindromes