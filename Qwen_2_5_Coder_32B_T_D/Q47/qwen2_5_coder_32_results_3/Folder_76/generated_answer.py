import re

def palindromes_of_specific_lengths(s):
    s = s[101:293].lower()
    r = re.compile('[^a-z]')
    s = r.sub('', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 153, min(i + 183, len(s)) + 1):
            candidate = s[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes