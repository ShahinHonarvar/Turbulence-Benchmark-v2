def filter_chars(s):
    t = set(s[4:5])
    return ''.join((c for c in s if c not in t or not '7' <= c <= 'o'))