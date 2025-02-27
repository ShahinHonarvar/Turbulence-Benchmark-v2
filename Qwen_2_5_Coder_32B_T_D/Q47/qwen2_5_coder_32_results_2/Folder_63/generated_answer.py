import re

def palindromes_of_specific_lengths(s):
    s = s[33:86].lower()
    r = re.compile('[^a-z]', re.IGNORECASE)
    s = r.sub('', s)
    palindromes = set()
    for length in range(26, 32):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes