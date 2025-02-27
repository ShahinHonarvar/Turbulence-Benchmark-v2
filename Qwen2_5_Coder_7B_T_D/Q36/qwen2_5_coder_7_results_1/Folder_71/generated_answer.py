def filter_chars(s):
    chars_to_remove = set((s[82:89] for _ in range(82, 89) if '*' < s[82:89] < '['))
    return ''.join((c for c in s if c not in chars_to_remove))