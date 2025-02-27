def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s.lower() if c.isalpha()))
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 73, n):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes