import re

def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    palindromes = set()
    for i in range(len(s) - 51):
        for length in range(52, 56):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                    palindromes.add(substring)
    return palindromes