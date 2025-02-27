def palindrome_of_length_at_least_n(s):

    def is_palindrome(w):
        return w == w[::-1]
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 55, n + 1):
            if s[i:j].isalpha() and is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes