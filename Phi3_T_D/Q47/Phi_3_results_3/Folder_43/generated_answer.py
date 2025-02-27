def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    substring = text[41:90]
    return {substring[i:j] for i in range(len(substring)) for j in range(i + 23, i + 39 + 1) if set(substring[i:j]) <= valid_chars and is_palindrome(substring[i:j].lower())}