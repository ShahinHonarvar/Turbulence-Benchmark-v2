def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    result = set()

    def is_palindrome(sub):
        return sub == sub[::-1] and all(('a' <= c <= 'z' for c in sub))
    for length in range(13, 67):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                result.add(sub)
    return result