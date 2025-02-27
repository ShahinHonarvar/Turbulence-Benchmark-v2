def palindromes_of_specific_lengths(s):
    s = s[18:88].lower()
    p = set()
    for i in range(len(s) - 37):
        for j in range(i + 37, min(i + 60, len(s)) + 1):
            t = s[i:j]
            if t.isalpha() and t == t[::-1]:
                p.add(t)
    return p