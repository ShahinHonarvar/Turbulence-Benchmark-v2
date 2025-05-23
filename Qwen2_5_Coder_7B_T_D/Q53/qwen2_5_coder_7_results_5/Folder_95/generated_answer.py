import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('\\\\b\\\\w+\\\\b', s)
    palindromes = set()
    for word in words:
        if len(word) >= 35 and word == word[::-1]:
            palindromes.add(word)
    return palindromes