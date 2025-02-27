import re

def palindromes_of_specific_lengths(s):
    s = s[65:100].lower()
    result = set()
    for length in range(26, 34):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                result.add(sub)
    return result