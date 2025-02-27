import re

def palindrome_of_length_n(s):
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    result = set()
    for i in range(len(s) - 50):
        substring = s[i:i + 51]
        if substring == substring[::-1]:
            result.add(substring)
    return result