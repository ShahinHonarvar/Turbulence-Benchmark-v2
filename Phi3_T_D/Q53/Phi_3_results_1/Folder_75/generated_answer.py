def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text_lower = text.lower()
    for i in range(len(text_lower)):
        for length in range(40, len(text_lower) - i + 1):
            word = text_lower[i:i + length]
            if word.isalpha() and is_palindrome(word):
                palindromes.add(word)
    return palindromes