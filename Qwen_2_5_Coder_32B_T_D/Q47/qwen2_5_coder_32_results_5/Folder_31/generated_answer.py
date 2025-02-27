def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    p = set()
    for i in range(len(s) - 36):
        for j in range(i + 37, min(i + 61, len(s)) + 1):
            t = s[i:j]
            if t.isalpha() and t == t[::-1]:
                p.add(t)
    return p