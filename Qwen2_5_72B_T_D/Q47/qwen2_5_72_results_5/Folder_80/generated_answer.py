def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def valid_char(c):
        return c.isalpha() and c.isascii()
    s = s[35:89]
    palindromes = set()
    for length in range(24, 34):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes