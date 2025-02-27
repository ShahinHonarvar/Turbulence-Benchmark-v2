def palindrome_of_length_at_least_n(s):
    set_of_palindromes = set()
    s = s.lower()

    def is_palindrome(substr):
        return substr == substr[::-1]
    for i in range(len(s)):
        for length in range(9, len(s) - i + 1):
            substr = s[i:i + length]
            if all((c.isalpha() for c in substr)) and is_palindrome(substr):
                set_of_palindromes.add(substr)
    return set_of_palindromes