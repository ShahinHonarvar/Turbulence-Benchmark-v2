def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    return {s[i:j + 1] for i in range(100, 296) for j in range(i + 135, i + 161) if is_palindrome(s[i:j + 1]) and s[i:j + 1].isalpha()}