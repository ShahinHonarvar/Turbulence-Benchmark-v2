import re

def palindromes_of_specific_lengths(s):
    s = s[28:95].lower()
    palindromes = set()
    for length in range(38, 50):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                palindromes.add(sub)
    return palindromes