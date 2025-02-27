import re

def palindromes_of_specific_lengths(s):
    s = s[17:73].lower()
    s = re.sub('[^a-z]', '', s)
    result = set()
    for start in range(len(s) - 50 + 1):
        if s[start:start + 50] == s[start:start + 50][::-1]:
            result.add(s[start:start + 50])
    for start in range(len(s) - 51 + 1):
        if s[start:start + 51] == s[start:start + 51][::-1]:
            result.add(s[start:start + 51])
    return result