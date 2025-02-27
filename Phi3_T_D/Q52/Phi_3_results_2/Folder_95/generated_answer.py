def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    res = set()
    s_lower = s.lower()
    for i in range(len(s) - 86):
        sub = s_lower[i:i + 87]
        if is_palindrome(sub):
            res.add(sub)
    return res