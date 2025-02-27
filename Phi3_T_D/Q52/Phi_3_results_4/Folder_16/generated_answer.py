def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(text):
    text = text.lower()
    length = 255
    palindromes = {text[i:i + length] for i in range(len(text) - length + 1) if 'a' <= text[i] <= 'z' and all((k.isalpha() for k in text[i:i + length])) and is_palindrome(text[i:i + length])}
    return palindromes