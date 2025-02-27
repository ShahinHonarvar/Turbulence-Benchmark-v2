def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 149, n):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes