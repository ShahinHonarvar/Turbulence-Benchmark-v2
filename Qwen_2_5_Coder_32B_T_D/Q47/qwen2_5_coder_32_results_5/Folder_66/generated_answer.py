import re

def palindromes_of_specific_lengths(s):
    s = s[32:80].lower()
    palindromes = set()
    for start in range(len(s) - 34):
        for length in range(35, 42):
            if start + length <= len(s):
                sub = s[start:start + length]
                if sub == sub[::-1] and re.match('^[a-z]+$', sub):
                    palindromes.add(sub)
    return palindromes