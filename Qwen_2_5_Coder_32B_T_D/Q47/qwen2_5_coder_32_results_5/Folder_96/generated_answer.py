import re

def palindromes_of_specific_lengths(s):
    s = s[100:301].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 50, min(i + 101, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                palindromes.add(sub)
    return palindromes