def palindrome_of_length_at_least_n(s):
    min_length = 77
    s = s.lower()
    palindromes = set()

    def is_palindrome(substr):
        return substr == substr[::-1]
    for start in range(len(s)):
        for end in range(start + min_length, len(s) + 1):
            if is_palindrome(s[start:end]):
                palindromes.add(s[start:end])
    return palindromes