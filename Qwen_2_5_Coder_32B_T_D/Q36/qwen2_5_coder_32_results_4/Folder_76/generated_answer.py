def filter_chars(s):
    chars_to_remove = set(s[669:888]) & set((chr(i) for i in range(ord('C'), ord('Y'))))
    return ''.join((c for c in s if c not in chars_to_remove))