def palindromes_of_specific_lengths(s):
    s = s[1:9].lower()
    p = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, i + 5):
            if j > len(s):
                break
            t = s[i:j]
            if t.isalpha() and t == t[::-1]:
                p.add(t)
    return p