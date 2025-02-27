def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(67, 90)))
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result