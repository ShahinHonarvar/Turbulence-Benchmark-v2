def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1] and all(('a' <= c.lower() <= 'z' for c in sub))
    s = s[29:99]
    return {s[i:i + length] for length in range(6, 10) for i in range(len(s) - length + 1) if is_palindrome(s[i:i + length])}