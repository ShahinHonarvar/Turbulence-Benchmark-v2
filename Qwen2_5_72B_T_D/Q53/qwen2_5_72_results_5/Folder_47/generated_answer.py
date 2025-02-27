def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()

    def is_alpha(c):
        return 'a' <= c <= 'z'
    for i in range(n):
        for j in range(i + 76, n + 1):
            if s[i:j] == s[i:j][::-1] and all((is_alpha(c) for c in s[i:j])):
                palindromes.add(s[i:j])
    return palindromes