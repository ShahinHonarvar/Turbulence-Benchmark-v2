import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('[a-z]{30,}', s)
    palindromes = {word for word in words if word == word[::-1]}
    return palindromes