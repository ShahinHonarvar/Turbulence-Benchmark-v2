import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-z]', '', s.lower())
    p = set()
    l = len(s)
    for i in range(l):
        for j in range(i + 28, l + 1):
            x = s[i:j]
            if x == x[::-1]:
                p.add(x)
    return p