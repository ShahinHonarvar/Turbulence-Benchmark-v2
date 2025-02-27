def filter_chars(s):
    if len(s) < 86:
        return s
    chars_to_remove = set(s[56:86]) & set((chr(i) for i in range(ord('+') + 1, ord('w'))))
    return ''.join((c for c in s if c not in chars_to_remove))