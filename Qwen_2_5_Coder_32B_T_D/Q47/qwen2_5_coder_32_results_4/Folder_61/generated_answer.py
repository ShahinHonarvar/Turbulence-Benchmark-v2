def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    p = set()
    for i in range(len(s) - 1):
        for j in range(i + 20, min(i + 31, len(s)) + 1):
            t = s[i:j]
            if t.isalpha() and t == t[::-1]:
                p.add(t)
    return p