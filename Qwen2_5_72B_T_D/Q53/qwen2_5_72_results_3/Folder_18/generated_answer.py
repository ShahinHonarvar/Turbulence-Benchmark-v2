def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n):
        for j in range(i + 61, n):
            if s[i:j + 1].isalpha() and is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes