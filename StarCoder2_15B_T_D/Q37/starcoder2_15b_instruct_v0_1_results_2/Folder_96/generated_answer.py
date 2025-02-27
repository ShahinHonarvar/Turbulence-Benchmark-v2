def filter_chars(s):
    new_chars = [c for c in s if c < '!' or c > 's' or s.index(c) < 86 or (s.index(c) > 92)]
    return ''.join(new_chars)