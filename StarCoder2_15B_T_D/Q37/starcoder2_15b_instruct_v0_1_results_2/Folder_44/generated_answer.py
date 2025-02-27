def filter_chars(s):
    filtered = [c for c in s if c < '+' or c > '8' or s.index(c) < 21 or (s.index(c) > 43)]
    return ''.join(filtered)