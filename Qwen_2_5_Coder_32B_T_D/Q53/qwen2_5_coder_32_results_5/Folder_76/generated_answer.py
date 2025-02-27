def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if sub.isalpha() and sub == sub[::-1] and (len(sub) >= 137):
                palindromes.add(sub)
    return palindromes