def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 139, len(s)):
            if is_palindrome(s[i:j + 1]):
                res.add(s[i:j + 1])
    return res