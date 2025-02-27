def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 49

    def is_palindrome(subs):
        return subs == subs[::-1]
    res = set()
    for i in range(len(s) - n + 1):
        if is_palindrome(s[i:i + n]):
            res.add(s[i:i + n])
    return res