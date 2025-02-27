def filter_chars(s):
    s = list(s)
    for i in range(56, 86):
        if '+' < s[i] < 'w':
            s = [c for c in s if c != s[i]]
    return ''.join(s)