def filter_chars(s):
    chars_to_remove = set(s[30:33]) & set((chr(c) for c in range(ord('%') + 1, ord('a'))))
    return ''.join((ch for ch in s if ch not in chars_to_remove))