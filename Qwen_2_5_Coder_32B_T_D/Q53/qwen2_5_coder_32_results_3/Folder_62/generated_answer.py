def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 31, n + 1):
            substr = ''.join(filter(str.isalpha, s[i:j]))
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes