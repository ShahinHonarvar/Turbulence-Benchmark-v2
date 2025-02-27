def filter_chars(s):
    t = set(s[69:81])
    r = [c for c in s if c not in t or not '@' <= c <= 'p']
    return ''.join(r)