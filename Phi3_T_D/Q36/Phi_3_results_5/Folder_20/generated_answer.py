def filter_chars(s):
    indices = slice(13, 40)
    chars_to_remove = set((c for c in s[indices] if ':' < c < 'C'))
    return ''.join((c for c in s if c not in chars_to_remove))