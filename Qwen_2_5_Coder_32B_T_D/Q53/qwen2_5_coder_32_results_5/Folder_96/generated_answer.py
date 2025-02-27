def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 24, n + 1):
            sub = s[i:j]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes