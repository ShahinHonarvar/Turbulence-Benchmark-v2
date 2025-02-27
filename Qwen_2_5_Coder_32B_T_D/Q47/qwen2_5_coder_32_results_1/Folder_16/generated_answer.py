import re

def palindromes_of_specific_lengths(s):
    s = s[15:87].lower()
    palindromes = set()
    for i in range(len(s) - 50):
        for j in range(51, 61):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                    palindromes.add(sub)
    return palindromes