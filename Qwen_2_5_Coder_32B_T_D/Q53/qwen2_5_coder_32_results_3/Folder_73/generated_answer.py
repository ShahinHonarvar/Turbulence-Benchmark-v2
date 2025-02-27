def palindrome_of_length_at_least_n(s):
    s = s.lower()
    l = len(s)
    p = set()
    for i in range(l - 93):
        for j in range(i + 94, l + 1):
            t = s[i:j]
            if t == t[::-1] and t.isalpha():
                p.add(t)
    return p