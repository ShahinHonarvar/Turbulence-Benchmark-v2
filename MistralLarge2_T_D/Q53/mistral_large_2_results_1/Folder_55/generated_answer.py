def palindrome_of_length_at_least_n(s):

    def is_palindrome(x):
        return x == x[::-1]
    n = 83
    s_lower = s.lower()
    palindromes = set()
    for i in range(len(s_lower)):
        for j in range(i + n, len(s_lower) + 1):
            if is_palindrome(s_lower[i:j]):
                palindromes.add(s_lower[i:j])
    return palindromes