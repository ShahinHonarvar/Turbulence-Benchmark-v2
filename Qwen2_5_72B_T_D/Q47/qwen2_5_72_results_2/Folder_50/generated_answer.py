def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def is_valid_char(c):
        return c.isalpha() and c.isascii()
    s = s[36:93]
    palindromes = set()
    for length in range(10, 36):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub) and all((is_valid_char(c) for c in sub)):
                palindromes.add(sub.lower())
    return palindromes