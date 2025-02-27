def is_valid_palindrome(s):
    return s.isalpha() and s == s[::-1]

def palindromes_of_specific_lengths(text):
    return {text[i:j + 1] for i in range(3, 301) for j in range(i, 301) if is_valid_palindrome(text[i:j + 1].lower()) and 3 <= len(text[i:j + 1]) <= 300}