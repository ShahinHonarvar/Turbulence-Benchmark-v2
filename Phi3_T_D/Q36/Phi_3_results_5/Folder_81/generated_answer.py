def filter_chars(s):
    start, end = (51, 77)
    to_filter = set((c for c in s[start:end] if '6' <= c <= 'e'))
    return ''.join((c for c in s if c not in to_filter))