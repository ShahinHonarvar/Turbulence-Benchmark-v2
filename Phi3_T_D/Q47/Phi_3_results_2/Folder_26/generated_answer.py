def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    substring = text[24:85]
    return {substring[i:i + length] for length in range(21, 32) for i in range(len(substring) - length + 1) if is_palindrome(substring[i:i + length]) and substring[i:i + length].isalpha()}