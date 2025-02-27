def filter_chars(s):
    chars_to_remove = set(s[476:948]) & set((c for c in range(ord('c'), ord('d'))))
    return ''.join((c for c in s if c not in chars_to_remove))