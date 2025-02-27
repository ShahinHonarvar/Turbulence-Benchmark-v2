import re

def palindromes_of_specific_lengths(s):
    s = s[30:85].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 11, min(i + 21, len(s) + 1)):
            sub = s[i:j]
            if re.fullmatch('[a-z]+', sub) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes