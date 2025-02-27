import re

def palindrome_of_length_n(s):
    s = s.lower()
    regex = re.compile('[^a-z]')
    s = regex.sub('', s)
    n = 420
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes