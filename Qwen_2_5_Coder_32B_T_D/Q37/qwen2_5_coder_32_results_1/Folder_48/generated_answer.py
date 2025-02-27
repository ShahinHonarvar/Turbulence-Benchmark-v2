def filter_chars(s):
    chars_to_remove = set(s[513:878]) & set((chr(x) for x in range(63, 110)))
    return ''.join((c for c in s if c not in chars_to_remove))