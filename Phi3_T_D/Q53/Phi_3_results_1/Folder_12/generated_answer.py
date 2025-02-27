def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 0
    start, end = (0, 0)
    while start + n < len(s):
        while end < len(s) and s[start + n] == s[end]:
            end += 1
        for m in range(n, end - start):
            if s[start + m] == s[start + n + end - m - 1]:
                palindromes.add(s[start + m:start + n + end - m])
        start += 1
        if end == len(s):
            end = start
    return {p for p in palindromes if len(p) >= 51}