def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 3):
        for j in range(i + 3, n + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes