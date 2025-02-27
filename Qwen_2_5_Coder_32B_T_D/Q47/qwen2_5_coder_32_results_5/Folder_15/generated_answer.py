import re

def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    regex = re.compile('[^a-z]')
    s = regex.sub('', s)
    p = set()
    for i in range(len(s)):
        for j in range(i + 2, min(i + 6, len(s)) + 1):
            t = s[i:j]
            if t == t[::-1]:
                p.add(t)
    return p