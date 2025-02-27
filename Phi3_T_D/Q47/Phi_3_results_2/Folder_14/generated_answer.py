import re

def palindromes_of_specific_lengths(s):
    s = s[10:75]
    s = re.sub('[^a-zA-Z]', '', s)
    res = set()
    for length in range(6, 9):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                res.add(substring.lower())
    return res