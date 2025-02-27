def filter_chars(s):
    remove_chars = set(s[35:99]) & set((chr(i) for i in range(ord('A'), ord('b') + 1)))
    return ''.join((c for c in s if c not in remove_chars))