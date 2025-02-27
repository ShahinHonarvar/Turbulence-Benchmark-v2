import re

def palindromes_of_specific_lengths(s):
    s = s[15:73]
    s = s.lower()
    palindromes = set()
    for length in range(19, 56):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if re.match('^[a-z]+$', sub) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes