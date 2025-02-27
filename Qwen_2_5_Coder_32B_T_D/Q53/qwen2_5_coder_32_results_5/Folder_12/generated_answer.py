def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 50, n):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes