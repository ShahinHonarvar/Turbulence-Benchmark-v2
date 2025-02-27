def filter_chars(s):
    to_remove = set((s[i] for i in range(15, 85) if 'I' < s[i] < 'M'))
    return ''.join((c for c in s if c not in to_remove))