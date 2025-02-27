def filter_chars(s):
    if len(s) < 754:
        return s
    chars_to_remove = set(s[503:754]) & set((chr(c) for c in range(ord('9'), ord('w') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))