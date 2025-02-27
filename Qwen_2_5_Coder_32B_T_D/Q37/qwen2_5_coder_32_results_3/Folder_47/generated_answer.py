def filter_chars(s):
    chars_to_remove = set(s[38:55]) & set((chr(x) for x in range(ord(':'), ord('r') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))