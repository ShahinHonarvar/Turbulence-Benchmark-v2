def filter_chars(s):
    chars_to_remove = set(s[379:899]) & set((chr(c) for c in range(ord('M'), ord('v') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))