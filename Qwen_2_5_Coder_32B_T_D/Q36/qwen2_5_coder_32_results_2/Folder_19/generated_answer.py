def filter_chars(s):
    chars_to_remove = set(s[78:87]) & set((chr(x) for x in range(ord(';') + 1, ord('r'))))
    return ''.join((c for c in s if c not in chars_to_remove))