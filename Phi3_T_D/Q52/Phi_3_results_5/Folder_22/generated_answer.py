def is_palindrome(s):
    return s == s[::-1]

def find_palindromes_of_length_n(s, n):
    return {s[i:i + n] for i in range(len(s) - n + 1) if is_palindrome(s[i:i + n])}

def palindrome_of_length_n(s):
    n = 20
    return find_palindromes_of_length_n(s.lower(), n)