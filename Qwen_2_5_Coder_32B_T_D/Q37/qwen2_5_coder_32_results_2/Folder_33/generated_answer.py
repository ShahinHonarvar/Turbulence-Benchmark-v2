def filter_chars(s):
    if len(s) < 833:
        return s
    target_chars = set(s[722:833]) & set((chr(i) for i in range(ord('K'), ord('m') + 1)))
    return ''.join((c for c in s if c not in target_chars))