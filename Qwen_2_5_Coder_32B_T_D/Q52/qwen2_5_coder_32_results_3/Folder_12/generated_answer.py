import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-z]', '', s.lower())
    n = 23
    result = set()
    for i in range(len(s) - n + 1):
        candidate = s[i:i + n]
        if candidate == candidate[::-1]:
            result.add(candidate)
    return result