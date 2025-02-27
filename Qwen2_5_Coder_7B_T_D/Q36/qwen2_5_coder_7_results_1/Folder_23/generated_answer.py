def filter_chars(s):
    filtered_chars = set((s[21:25] if '5' < c < '}' else '' for c in s[21:25]))
    return ''.join((c for c in s if c not in filtered_chars))