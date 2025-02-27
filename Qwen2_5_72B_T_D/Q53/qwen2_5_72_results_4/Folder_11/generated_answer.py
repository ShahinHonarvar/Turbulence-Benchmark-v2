def palindrome_of_length_at_least_n(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    n = 54
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes