def filter_chars(s):
    to_remove = set((c for c in s[86:93] if '!' <= c <= 's'))
    return ''.join((c for c in s if c not in to_remove))