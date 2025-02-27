def filter_chars(s):
    if len(s) < 89:
        return s
    target_chars = set(s[12:89]) & set((chr(c) for c in range(ord('&'), ord('v') + 1)))
    return ''.join((c for c in s if c not in target_chars))