def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    n = 93
    s = ''.join([c for c in s if c.isalpha()])
    return {s[i:i + n].lower() for i in range(len(s) - n + 1) if is_palindrome(s[i:i + n])}