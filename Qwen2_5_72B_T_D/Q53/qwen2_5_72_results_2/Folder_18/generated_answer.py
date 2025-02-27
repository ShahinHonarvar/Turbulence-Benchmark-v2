def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n):
        for j in range(i + 61, n + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes