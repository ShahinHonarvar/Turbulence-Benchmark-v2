def palindrome_of_length_n(s):
    s = s.lower()
    p = set()
    for i in range(len(s) - 185):
        t = s[i:i + 186]
        if t == t[::-1] and t.isalpha():
            p.add(t)
    return p