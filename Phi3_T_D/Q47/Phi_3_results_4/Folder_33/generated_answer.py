import re

def palindromes_of_specific_lengths(s):
    s = s[130:296].lower()
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for length in range(103, 159):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if re.match('^[a-z]+$', substr) and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes