import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('\\\\b\\\\w+\\\\b', s)
    palindrome_set = set()
    for word in words:
        if len(word) >= 35 and word == word[::-1]:
            palindrome_set.add(word)
    return palindrome_set