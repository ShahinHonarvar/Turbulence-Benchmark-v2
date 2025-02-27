import re

def palindromes_of_specific_lengths(s):
    s = s[17:73].lower()
    s = re.sub('[^a-z]', '', s)
    l = set()
    for i in range(len(s) - 49):
        if s[i:i + 50] == s[i:i + 50][::-1]:
            l.add(s[i:i + 50])
        if i + 51 <= len(s) and s[i:i + 51] == s[i:i + 51][::-1]:
            l.add(s[i:i + 51])
    return l