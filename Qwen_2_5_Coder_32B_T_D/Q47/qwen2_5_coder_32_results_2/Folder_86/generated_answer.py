import re

def palindromes_of_specific_lengths(s):
    s = s[30:96].lower()
    palindromes = set()
    for i in range(len(s)):
        for l in range(34, 56):
            if i + l <= len(s):
                substring = s[i:i + l]
                if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                    palindromes.add(substring)
    return palindromes