def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = ''.join((c for c in s if c.isalpha())).lower()
    n = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n):
        for j in range(i + 11, n + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes