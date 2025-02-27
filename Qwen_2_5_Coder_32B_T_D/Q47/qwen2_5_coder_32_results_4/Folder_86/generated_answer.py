import re

def palindromes_of_specific_lengths(s):
    ss = s[30:96].lower()
    palindromes = set()
    for i in range(len(ss) - 33):
        for j in range(i + 34, min(i + 56, len(ss)) + 1):
            sub = re.sub('[^a-z]', '', ss[i:j])
            if sub and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes