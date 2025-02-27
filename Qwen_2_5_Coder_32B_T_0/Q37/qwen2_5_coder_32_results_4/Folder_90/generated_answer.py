def filter_chars(s):
    if len(s) < 853:
        return s
    chars_to_remove = set(s[348:853]) & set((chr(i) for i in range(ord('J'), ord('b') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))