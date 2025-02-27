def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 84 + 1):
        for j in range(i + 84, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes