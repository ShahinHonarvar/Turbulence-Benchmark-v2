def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 47):
        for j in range(i + 48, n + 1):
            candidate = s[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes