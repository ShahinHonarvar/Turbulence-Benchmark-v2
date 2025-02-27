import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('[a-z]+', s)
    palindromes = set()
    for word in words:
        if len(word) >= 44 and word == word[::-1]:
            palindromes.add(word)
    return palindromes