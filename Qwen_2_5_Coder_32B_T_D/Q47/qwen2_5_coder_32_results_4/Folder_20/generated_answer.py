import re

def palindromes_of_specific_lengths(s):
    s = s[20:75].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s) - 35):
        for l in range(36, 43):
            if i + l <= len(s):
                substring = s[i:i + l]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes