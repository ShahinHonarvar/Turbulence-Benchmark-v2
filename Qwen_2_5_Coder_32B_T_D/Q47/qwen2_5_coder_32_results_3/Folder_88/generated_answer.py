import re

def palindromes_of_specific_lengths(s):
    s = s[11:88].lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, i + 6):
            if j <= len(s):
                sub = s[i:j]
                if sub == sub[::-1] and re.match('^[a-z]+$', sub):
                    palindromes.add(sub)
    return palindromes