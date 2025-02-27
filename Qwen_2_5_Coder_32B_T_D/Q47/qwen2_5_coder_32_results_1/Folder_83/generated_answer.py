def palindromes_of_specific_lengths(s):
    s = s[75:96].lower()
    p = set()
    for i in range(len(s) - 6):
        for l in range(7, 10):
            if i + l <= len(s):
                w = s[i:i + l]
                if w.isalpha() and w == w[::-1]:
                    p.add(w)
    return p