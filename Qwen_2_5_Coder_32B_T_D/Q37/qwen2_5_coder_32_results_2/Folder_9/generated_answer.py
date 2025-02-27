def filter_chars(s):
    chars_to_remove = set(s[38:100]) & set((chr(i) for i in range(ord('A'), ord('Q') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))