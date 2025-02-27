import re

def palindromes_of_specific_lengths(s):
    s = s[26:91].lower()
    p = re.compile('[^a-z]')
    s = p.sub('', s)
    result = set()
    for i in range(len(s)):
        for j in range(i + 27, min(i + 59, len(s)) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result