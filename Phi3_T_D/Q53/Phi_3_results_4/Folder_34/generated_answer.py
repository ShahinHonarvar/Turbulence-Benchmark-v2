def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pals = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 68, n + 1):
            substr = s[i:j]
            if substr == substr[::-1] and all((c.isalpha() for c in substr)):
                pals.add(substr)
    return pals