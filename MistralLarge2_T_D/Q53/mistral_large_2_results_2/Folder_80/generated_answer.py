def palindrome_of_length_at_least_n(s):
    n = 30
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for length in range(n, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes