def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 90, n + 1):
            substring = ''.join(filter(str.isalpha, s[i:j]))
            if substring == substring[::-1] and len(substring) >= 90:
                palindromes.add(substring)
    return palindromes