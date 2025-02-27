def filter_chars(s):
    t = s[138:921]
    chars_to_remove = set((c for c in t if '6' <= c <= 'A'))
    return ''.join((c for c in s if c not in chars_to_remove))