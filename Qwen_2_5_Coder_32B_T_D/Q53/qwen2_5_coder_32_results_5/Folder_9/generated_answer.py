def palindrome_of_length_at_least_n(s):
    s = s.lower()
    p = set()
    for i in range(len(s)):
        for j in range(i + 95, len(s) + 1):
            t = s[i:j]
            if t == t[::-1] and t.isalpha():
                p.add(t)
    return p