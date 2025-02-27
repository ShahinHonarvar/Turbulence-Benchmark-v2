import re

def palindromes_of_specific_lengths(s):
    s = s[16:95].lower()
    palindromes = set()
    for i in range(len(s) - 38):
        for j in range(i + 39, min(i + 53, len(s)) + 1):
            sub = s[i:j]
            if re.fullmatch('[a-z]+', sub) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes