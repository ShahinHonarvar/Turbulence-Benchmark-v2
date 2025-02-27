import re

def palindromes_of_specific_lengths(s):
    s = s[18:89].lower()
    palindromes = set()
    for i in range(len(s) - 11):
        for j in range(i + 12, i + 15):
            if j > len(s):
                break
            sub = s[i:j]
            if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                palindromes.add(sub)
    return palindromes