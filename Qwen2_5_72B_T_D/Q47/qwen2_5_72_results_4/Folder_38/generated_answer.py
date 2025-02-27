def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def is_valid_char(c):
        return c.isalpha() and (65 <= ord(c) <= 90 or 97 <= ord(c) <= 122)
    s = s[18:88]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 38, min(i + 61, len(s) + 1)):
            sub = s[i:j]
            if is_palindrome(sub) and all((is_valid_char(c) for c in sub)):
                palindromes.add(sub)
    return palindromes