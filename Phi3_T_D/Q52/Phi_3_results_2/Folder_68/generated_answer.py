def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    return {s[i:i + 76] for i in range(len(s) - 75) if s[i:i + 76].isalpha() and is_palindrome(s[i:i + 76])}