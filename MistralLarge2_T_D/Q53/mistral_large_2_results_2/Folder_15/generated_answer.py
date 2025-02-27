def palindrome_of_length_at_least_n(s):

    def is_palindrome(x):
        return x == x[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for i in range(n):
        for j in range(i + 4, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes