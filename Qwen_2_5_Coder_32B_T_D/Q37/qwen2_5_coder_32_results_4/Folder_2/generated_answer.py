def filter_chars(s):
    t = s[477:985]
    chars_to_remove = set((c for c in t if ',' <= c <= 'V'))
    return ''.join((c for c in s if c not in chars_to_remove))