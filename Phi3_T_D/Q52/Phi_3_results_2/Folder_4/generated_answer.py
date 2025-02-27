def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    res = set()
    s = s.lower()
    for i in range(len(s) - 14):
        sub = s[i:i + 15]
        if all((c.isalpha() for c in sub)) and is_palindrome(sub):
            res.add(sub)
    return res