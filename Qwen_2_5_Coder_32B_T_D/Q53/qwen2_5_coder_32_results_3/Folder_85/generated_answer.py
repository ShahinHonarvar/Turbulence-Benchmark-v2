def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 85, n + 1):
            sub = s[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes