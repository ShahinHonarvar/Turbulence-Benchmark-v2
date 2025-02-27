def filter_chars(s):
    chars_to_remove = set(s[503:754]) & set((chr(i) for i in range(ord('9'), ord('w') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))