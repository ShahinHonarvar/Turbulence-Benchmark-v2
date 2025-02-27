def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        start = i
        end = i + 67
        if end <= n:
            substring = s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes