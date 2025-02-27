import re

def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(18, 89 - 14 + 1):
        for l in range(12, 15):
            sub = s[i:i + l].lower()
            if re.fullmatch('[a-z]*', sub) and sub == sub[::-1]:
                result.add(sub)
    return result