def palindrome_of_length_n(s):

    def is_palindrome(sub_s):
        return sub_s == sub_s[::-1]
    s = s.lower()
    n = 21
    return {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n].isalpha() and is_palindrome(s[i:i + n])}