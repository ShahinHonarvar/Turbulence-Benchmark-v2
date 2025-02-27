def filter_chars(s):
    return s[0:3] + ''.join([c for i, c in enumerate(s) if (i < 3 or i > 8) or '?' < c < 'k'])