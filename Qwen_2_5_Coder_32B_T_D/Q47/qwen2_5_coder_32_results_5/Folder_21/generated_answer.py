import re

def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    palindromes = set()
    for start in range(len(s) - 135):
        for length in range(136, 161):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                    palindromes.add(substring)
    return palindromes