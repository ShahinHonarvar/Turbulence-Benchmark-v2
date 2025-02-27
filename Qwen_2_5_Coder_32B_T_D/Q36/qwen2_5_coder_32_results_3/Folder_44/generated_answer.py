def filter_chars(s):
    chars_to_remove = set(s[18:64]) & set((chr(i) for i in range(ord('4'), ord('B'))))
    return ''.join((c for c in s if c not in chars_to_remove))