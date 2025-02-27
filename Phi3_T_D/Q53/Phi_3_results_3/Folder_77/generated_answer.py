def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(n):
        for length in range(149, n - i + 1):
            if is_palindrome(s[i:i + length]) and s[i:i + length].isalpha():
                palindromes.add(s[i:i + length])
    return palindromes