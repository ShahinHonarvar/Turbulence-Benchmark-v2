def filter_chars(s):
    if len(s) < 853:
        return s
    target_chars = set(s[348:853]) & set((chr(i) for i in range(ord('J'), ord('b') + 1)))
    return ''.join((c for c in s if c not in target_chars))