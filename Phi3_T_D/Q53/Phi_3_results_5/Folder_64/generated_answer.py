def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    N = len(s)
    for i in range(N):
        for j in range(i + 9, N + 1):
            substr = s[i:j]
            if len(set(substr) - set('abcdefghijklmnopqrstuvwxyz')) == 0 and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes