def filter_chars(s):
    chars_to_remove = set((chr(c) for c in range(ord('W'), ord('[') + 1)))
    return ''.join((c for c in s[18:82] if c not in chars_to_remove))