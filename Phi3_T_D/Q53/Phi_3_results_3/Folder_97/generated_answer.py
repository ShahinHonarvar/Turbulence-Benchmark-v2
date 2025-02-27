def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(substr):
        return substr == substr[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 138, length + 1):
            substr = s[i:j]
            if all((c.isalpha() for c in substr)) and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes