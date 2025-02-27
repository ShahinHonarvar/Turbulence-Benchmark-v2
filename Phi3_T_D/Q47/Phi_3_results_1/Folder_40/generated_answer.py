def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    substring = text[:6]
    letters_only = ''.join([i.lower() for i in substring if i.isalpha()])
    return {letters_only[i:j] for i in range(len(letters_only)) for j in range(i + 3, i + 6) if is_palindrome(letters_only[i:j])}