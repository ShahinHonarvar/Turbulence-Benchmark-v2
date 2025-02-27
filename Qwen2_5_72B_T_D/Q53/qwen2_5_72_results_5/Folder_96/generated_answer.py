def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 24, n + 1):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes