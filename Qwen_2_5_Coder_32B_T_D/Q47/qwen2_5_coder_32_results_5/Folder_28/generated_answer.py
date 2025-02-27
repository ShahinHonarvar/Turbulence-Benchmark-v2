import re

def palindromes_of_specific_lengths(s):
    s = s[32:72]
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    result = set()
    for i in range(len(s) - 21 + 1):
        for j in range(21, 33):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1]:
                    result.add(substring)
    return result