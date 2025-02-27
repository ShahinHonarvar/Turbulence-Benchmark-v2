import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[22:96].lower()
    for i in range(len(substring)):
        for j in range(i + 52, min(i + 56, len(substring) + 1)):
            sub = substring[i:j]
            if re.fullmatch('[a-z]+', sub) and sub == sub[::-1]:
                result.add(sub)
    return result