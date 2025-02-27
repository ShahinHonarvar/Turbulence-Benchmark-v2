def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    n = 30
    while n <= len(s):
        for i in range(len(s) - n + 1):
            substring = s[i:i + n]
            if substring == substring[::-1]:
                palindromes.add(substring)
        n += 1
    return palindromes