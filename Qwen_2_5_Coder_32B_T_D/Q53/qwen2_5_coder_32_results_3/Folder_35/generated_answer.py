def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 25, n):
            substr = s[i:j + 1]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes