def filter_chars(s):
    return s[:5] + ''.join((c for c in s[6:] if c < 'G' or c > 'p'))