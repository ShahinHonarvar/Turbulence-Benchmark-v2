def palindromes_of_specific_lengths(s):
    s = s[2:9].lower()
    p = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, i + 5):
            w = s[i:j]
            if len(w) in [3, 4] and w.isalpha() and (w == w[::-1]):
                p.add(w)
    return p