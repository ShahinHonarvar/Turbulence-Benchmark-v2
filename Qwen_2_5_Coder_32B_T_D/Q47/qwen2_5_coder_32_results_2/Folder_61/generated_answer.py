import re

def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 19, 31):
            sub = s[i:j + 1]
            if re.match('^[a-z]+$', sub) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes