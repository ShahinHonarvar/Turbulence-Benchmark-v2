import re

def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    p = set()
    for i in range(len(s) - 56):
        for l in range(57, 61):
            if i + l > len(s):
                break
            sub = s[i:i + l]
            if re.fullmatch('[a-z]+', sub) and sub == sub[::-1]:
                p.add(sub)
    return p