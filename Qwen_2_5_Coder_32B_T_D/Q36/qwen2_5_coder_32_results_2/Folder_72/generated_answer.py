def filter_chars(s):
    chars_to_remove = set(s[44:68]) & set((chr(i) for i in range(ord('Y'), ord('x'))))
    return ''.join((c for c in s if c not in chars_to_remove))