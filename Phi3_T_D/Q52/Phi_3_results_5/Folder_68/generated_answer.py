def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    return {s[i:i + 76] for i in range(len(s) - 75) if is_palindrome(s[i:i + 76])}