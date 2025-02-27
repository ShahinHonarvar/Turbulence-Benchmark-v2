import re

def palindromes_of_specific_lengths(s):
    s = s[12:123].lower()
    regex = re.compile('[^a-z]')
    s = regex.sub('', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 12, min(i + 221, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes