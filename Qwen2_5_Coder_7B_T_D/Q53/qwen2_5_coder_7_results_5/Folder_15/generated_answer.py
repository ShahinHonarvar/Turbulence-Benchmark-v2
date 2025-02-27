def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 4
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= n:
                palindromes.add(substring)
    return palindromes