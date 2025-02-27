import string

def is_palindrome(s):
    return s == s[::-1] and all((c in string.ascii_letters for c in s))

def palindrome_of_length_n(s):
    s = s.lower()
    return set((s[i:i + 43] for i in range(len(s) - 42) if is_palindrome(s[i:i + 43])))