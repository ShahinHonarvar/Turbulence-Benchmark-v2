def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    for i in range(n):
        for j in range(i + 119, n + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes