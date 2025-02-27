def filter_chars(s):
    if len(s) < 878:
        return s
    chars_to_remove = set(s[513:878]) & set((chr(i) for i in range(63, 111)))
    return ''.join((c for c in s if c not in chars_to_remove))