def palindrome_of_length_n(s):
    n = 92
    s = s.lower()

    def is_palindrome(s):
        return s == s[::-1]
    return {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n].isalpha() and is_palindrome(s[i:i + n])}