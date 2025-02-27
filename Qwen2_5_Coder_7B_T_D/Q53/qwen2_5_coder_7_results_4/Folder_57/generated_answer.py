import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    words = re.findall('\\\\b\\\\w+\\\\b', s)
    for word in words:
        if len(word) >= 93 and word == word[::-1]:
            palindromes.add(word)
    return palindromes