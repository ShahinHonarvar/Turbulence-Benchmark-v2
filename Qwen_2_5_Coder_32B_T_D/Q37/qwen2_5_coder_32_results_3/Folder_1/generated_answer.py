def filter_chars(s):
    t = s[41:80]
    chars_to_remove = set((c for c in t if 'f' <= c <= '|'))
    return ''.join((c for c in s if c not in chars_to_remove))