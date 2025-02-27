def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 59
    palindromes = set()
    for i in range(len(s)):
        for length in range(n, len(s) + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and len(substr) >= n:
                palindromes.add(substr)
    return palindromes