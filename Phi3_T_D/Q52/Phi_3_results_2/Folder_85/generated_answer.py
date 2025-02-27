def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1] and all((c.isalpha() for c in sub))
    s = s.lower()
    return {s[i:i + 46].upper() for i in range(len(s) - 45) if is_palindrome(s[i:i + 46])}