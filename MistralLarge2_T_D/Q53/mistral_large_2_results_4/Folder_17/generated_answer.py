import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 36, length + 1):
            substring = s[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes