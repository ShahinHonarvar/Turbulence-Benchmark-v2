def filter_chars(s):
    to_remove = set((s[i] for i in range(23, 90) if 'w' <= s[i] <= '{'))
    return ''.join((c for c in s if c not in to_remove))