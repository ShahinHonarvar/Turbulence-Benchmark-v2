import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(w):
        return w.lower() == w.lower()[::-1]
    words = re.findall('\\b[a-zA-Z]+\\b', s)
    return {word for word in words if is_palindrome(word) and len(word) >= 77}