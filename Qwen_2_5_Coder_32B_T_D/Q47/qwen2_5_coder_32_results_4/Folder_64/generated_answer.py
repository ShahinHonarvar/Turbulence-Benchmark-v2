def palindromes_of_specific_lengths(s):
    s = s[:8].lower()
    p = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, min(i + 6, len(s)) + 1):
            t = s[i:j]
            if t.isalpha() and t == t[::-1]:
                p.add(t)
    return p