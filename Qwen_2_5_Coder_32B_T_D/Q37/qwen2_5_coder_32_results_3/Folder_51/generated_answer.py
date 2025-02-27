def filter_chars(s):
    t = s[36:41]
    chars_to_remove = set((c for c in t if 'H' <= c <= 'e'))
    return ''.join((c for c in s if c not in chars_to_remove))