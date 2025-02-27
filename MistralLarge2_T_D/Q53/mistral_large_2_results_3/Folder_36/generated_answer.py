def palindrome_of_length_at_least_n(s):

    def is_palindrome(x):
        return x.lower() == x.lower()[::-1]
    n = 144
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes