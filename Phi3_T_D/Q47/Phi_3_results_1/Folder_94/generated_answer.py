def is_palindrome(s):
    return s == s[::-1]

def valid_char(c):
    return 'a' <= c <= 'z'

def palindromes_of_specific_lengths(text):
    palindromes_set = set()
    for length in range(45, 52):
        for i in range(40, 95 - length + 1):
            substr = text[i:i + length].lower()
            if all((valid_char(c) for c in substr)) and is_palindrome(substr):
                palindromes_set.add(substr)
    return palindromes_set