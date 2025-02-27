def filter_chars(s):
    s = list(s)
    for i in range(40, 63):
        if s[i] > '7' and s[i] < 'H':
            s = [c for c in s if c != s[i]]
    return ''.join(s)