def filter_chars(s):
    chars_to_remove = set(s[19:93].intersection(set((chr(x) for x in range(ord('8'), ord('m') + 1)))))
    return ''.join((c for c in s if c not in chars_to_remove))