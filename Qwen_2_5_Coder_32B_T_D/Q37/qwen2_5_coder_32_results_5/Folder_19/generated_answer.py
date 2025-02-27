def filter_chars(s):
    t = s[35:90]
    chars_to_remove = set((c for c in t if 'E' <= c <= 't'))
    return ''.join((c for c in s if c not in chars_to_remove))