import re

def palindromes_of_specific_lengths(s):
    s = s[23:78].lower()
    r = re.compile('[^a-z]')
    palindromes = set()
    for i in range(len(s) - 12):
        for j in range(i + 13, min(i + 41, len(s) + 1)):
            sub = r.sub('', s[i:j])
            if sub == sub[::-1] and len(sub) >= 13 and (len(sub) <= 40):
                palindromes.add(sub)
    return palindromes