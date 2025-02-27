def filter_chars(s):
    if len(s) <= 753:
        return s
    chars_to_remove = set(s[503:754]) & set((chr(i) for i in range(57, 119)))
    return ''.join((c for c in s if c not in chars_to_remove))