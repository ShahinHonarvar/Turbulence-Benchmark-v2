def filter_chars(s):
    t = [c for i, c in enumerate(s) if not 50 <= ord(c) <= 80 or (c < 'A' or c > 'Q')]
    return ''.join(t)