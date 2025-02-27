def filter_chars(s):
    chars_to_remove = set(s[31:73] & set((chr(x) for x in range(ord('N'), ord('j')))))
    return ''.join((c for c in s if c not in chars_to_remove))