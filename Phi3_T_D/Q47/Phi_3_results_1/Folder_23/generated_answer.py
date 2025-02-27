def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    substring = s[23:95]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = {substring[i:j] for i in range(len(substring) - 16) for j in range(i + 17, 56) if all((c in english_letters for c in substring[i:j])) and is_palindrome(substring[i:j].lower())}
    return palindromes