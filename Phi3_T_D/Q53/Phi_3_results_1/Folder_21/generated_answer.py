import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 112, len(s) + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes