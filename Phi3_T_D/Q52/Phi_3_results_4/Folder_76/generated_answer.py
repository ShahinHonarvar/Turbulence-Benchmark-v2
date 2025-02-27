def palindrome_of_length_n(text):

    def is_valid_palindrome(s):
        return s == s[::-1]

    def valid_chars(s):
        return all(('a' <= c <= 'z' or 'A' <= c <= 'Z' for c in s))
    text = text.lower()
    palindromes = {text[i:i + 257] for i in range(len(text) - 256) if valid_chars(text[i:i + 257]) and is_valid_palindrome(text[i:i + 257])}
    return palindromes