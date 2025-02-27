import re

def palindromes_of_specific_lengths(s):
    s = s[18:89].lower()
    palindromes = set()
    for i in range(len(s) - 11):
        for length in range(12, 15):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                    palindromes.add(substring)
    return palindromes