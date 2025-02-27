import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    words = re.findall('\\b[a-zA-Z]+\\b', s.lower())
    palindromes = {word for word in words if is_palindrome(word) and len(word) >= 112}
    return palindromes