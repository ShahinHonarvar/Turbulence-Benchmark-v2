def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 13
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes