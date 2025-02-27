import re

def palindromes_of_specific_lengths(s):
    s = s[24:85].lower()
    pattern = re.compile('[a-z]{21,31}')
    words = pattern.findall(s)
    palindromes = {word for word in words if word == word[::-1]}
    return palindromes