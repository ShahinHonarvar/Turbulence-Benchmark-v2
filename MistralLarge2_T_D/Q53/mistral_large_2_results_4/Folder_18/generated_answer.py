import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    words = re.findall('\\b[a-zA-Z]+\\b', s)
    palindromes = {word for word in words if is_palindrome(word) and len(word) >= 62}
    return palindromes