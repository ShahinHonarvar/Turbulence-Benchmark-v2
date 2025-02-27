def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 144, n + 1):
            subs = s[i:j]
            if subs == subs[::-1] and all((c.isalpha() for c in subs)):
                palindromes.add(subs)
    return palindromes