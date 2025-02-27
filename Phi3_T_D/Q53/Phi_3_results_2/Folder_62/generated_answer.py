def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    set_palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 30, len(s) + 1):
            substr = s[i:j]
            if all((c.isalpha() for c in substr)) and is_palindrome(substr):
                set_palindromes.add(substr)
    return set_palindromes