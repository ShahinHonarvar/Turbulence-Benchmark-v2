def filter_chars(s):
    return s[:23] + ''.join((c for c in s[23:90] if not 'w' <= c <= '}')) + s[90:]