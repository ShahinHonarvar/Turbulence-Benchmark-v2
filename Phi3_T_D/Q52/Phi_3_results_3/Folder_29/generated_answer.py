def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    return {text[i:i + 19].lower() for i in range(len(text) - 18) if is_palindrome(text[i:i + 19].lower())}