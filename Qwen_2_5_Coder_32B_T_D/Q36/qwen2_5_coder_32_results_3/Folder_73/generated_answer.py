def filter_chars(s):
    t = ''.join(set(s[66:90]) & set((c for c in range(ord('#') + 1, ord('T')))))
    return ''.join((c for c in s if c not in t))