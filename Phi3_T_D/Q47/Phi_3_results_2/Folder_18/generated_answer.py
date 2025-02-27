import re

def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    candidate = text[10:84]
    candidate = re.sub('[^a-zA-Z]', '', candidate).lower()
    palindromes = set()
    for length in range(13, 67):
        for start in range(len(candidate) - length + 1):
            substring = candidate[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes