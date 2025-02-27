def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 19, n):
            substr = s[i:j + 1]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes