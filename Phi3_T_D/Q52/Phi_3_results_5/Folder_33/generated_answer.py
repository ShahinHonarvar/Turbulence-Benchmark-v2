def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(s) - 474):
        substr = s[i:i + 475]
        if all((c.isalpha() for c in substr)) and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes