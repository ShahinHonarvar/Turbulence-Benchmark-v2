def filter_chars(s):
    chars_to_remove = set(s[154:222]) & set((chr(c) for c in range(ord('A') + 1, ord('f'))))
    return ''.join((c for c in s if c not in chars_to_remove))