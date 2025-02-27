def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    substring = s[30:91].lower()
    palindromes = {substring[i:i + length] for length in range(50, 54) for i in range(len(substring) - length + 1) if substring[i:i + length].isalpha() and is_palindrome(substring[i:i + length])}
    return palindromes