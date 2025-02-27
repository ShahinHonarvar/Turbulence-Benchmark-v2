def filter_chars(s):
    chars_to_remove = set(s[42:98]) & set((chr(c) for c in range(ord('*'), ord('b') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))