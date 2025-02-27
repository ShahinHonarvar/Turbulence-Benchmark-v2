def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 112
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            candidate = s[i:j]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes