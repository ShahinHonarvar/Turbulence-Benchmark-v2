def filter_chars(s):
    t = s[71:97]
    characters_to_remove = set((c for c in t if '_' <= c <= 'o'))
    return ''.join((c for c in s if c not in characters_to_remove))