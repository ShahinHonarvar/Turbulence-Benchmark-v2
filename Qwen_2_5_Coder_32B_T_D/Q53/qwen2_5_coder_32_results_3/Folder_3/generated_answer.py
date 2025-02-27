def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 59, n + 1):
            seg = s[i:j]
            if seg.isalpha() and seg == seg[::-1]:
                palindromes.add(seg)
    return palindromes