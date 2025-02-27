def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 40, n + 1):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes