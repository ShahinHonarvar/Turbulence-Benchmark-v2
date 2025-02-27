import re

def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    palindromes = set()
    for i in range(len(s) - 56):
        for length in range(57, 61):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                    palindromes.add(substring)
    return palindromes