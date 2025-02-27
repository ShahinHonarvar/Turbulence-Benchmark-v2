def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 10, n + 1):
            candidate = s[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes