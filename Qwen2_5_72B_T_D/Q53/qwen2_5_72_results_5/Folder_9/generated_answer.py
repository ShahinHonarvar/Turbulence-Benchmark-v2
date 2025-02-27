def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 94, n):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes