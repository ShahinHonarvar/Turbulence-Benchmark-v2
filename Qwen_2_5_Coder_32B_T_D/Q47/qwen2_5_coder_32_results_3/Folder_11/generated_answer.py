import re

def palindromes_of_specific_lengths(s):
    s = s[24:98].lower()
    regex = re.compile('[^a-z]')
    s = regex.sub('', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 10, min(i + 37, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes