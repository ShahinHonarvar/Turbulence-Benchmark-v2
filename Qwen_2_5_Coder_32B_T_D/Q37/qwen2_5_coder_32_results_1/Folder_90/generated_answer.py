def filter_chars(s):
    if len(s) < 853:
        return s
    targets = set(s[348:853]) & set((chr(i) for i in range(ord('J'), ord('c'))))
    return ''.join((c for c in s if c not in targets))