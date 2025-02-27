def palindrome_of_length_at_least_n(s):

    def is_palindrome(x):
        return x == x[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    min_length = 94
    found_palindromes = set()
    for i in range(n):
        for j in range(i + min_length, n + 1):
            if is_palindrome(s[i:j]):
                found_palindromes.add(s[i:j])
    return found_palindromes