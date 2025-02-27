def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    return {s[i:i + 56] for i in range(len(s) - 55) if is_palindrome(s[i:i + 56])}