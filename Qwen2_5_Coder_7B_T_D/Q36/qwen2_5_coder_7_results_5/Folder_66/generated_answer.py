def filter_chars(s):
    filtered_chars = set((s[39:87] if '!' < c < '}' else '' for c in s[39:87]))
    return ''.join((c for c in s if c not in filtered_chars))