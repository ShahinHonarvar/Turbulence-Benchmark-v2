def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    s = ''.join((c for c in s if c.isalpha())).lower()
    n = len(s)
    for length in range(52, n + 1):
        for i in range(n - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes