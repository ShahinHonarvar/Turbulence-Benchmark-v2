def filter_chars(s):
    t = ''.join(s[27:75])
    chars_to_remove = set((c for c in t if 'A' < c < 'i'))
    return ''.join((c for c in s if c not in chars_to_remove))