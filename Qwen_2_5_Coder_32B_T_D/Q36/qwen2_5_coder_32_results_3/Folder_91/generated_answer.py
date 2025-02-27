def filter_chars(s):
    t = [c for c in s[:4] if '$' < c < '?']
    return ''.join((c for c in s if c not in t))