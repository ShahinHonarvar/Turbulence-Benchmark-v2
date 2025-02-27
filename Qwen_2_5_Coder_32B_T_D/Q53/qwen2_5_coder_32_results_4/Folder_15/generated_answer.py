def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for start in range(n):
        for end in range(start + 4, n + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes