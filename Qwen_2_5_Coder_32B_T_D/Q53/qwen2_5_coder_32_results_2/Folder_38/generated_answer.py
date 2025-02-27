import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    words = re.findall('[a-z]+', s)
    for word in words:
        if len(word) >= 56 and word == word[::-1]:
            palindromes.add(word)
    return palindromes