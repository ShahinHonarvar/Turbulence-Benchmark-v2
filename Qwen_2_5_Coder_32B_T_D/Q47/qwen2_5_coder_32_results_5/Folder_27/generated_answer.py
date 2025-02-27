import re

def palindromes_of_specific_lengths(s):
    s = s[13:100].lower()
    palindromes = set()
    for i in range(len(s) - 25):
        for l in range(26, 30):
            if i + l <= len(s):
                substring = s[i:i + l]
                if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                    palindromes.add(substring)
    return palindromes