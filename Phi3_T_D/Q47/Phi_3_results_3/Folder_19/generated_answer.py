def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    return {text[start:end] for start in range(10, 56) for end in range(start + 3, min(start + 8, 56) + 1) if text[start:end].isalpha() and text[start:end].islower() and is_palindrome(text[start:end].lower())}