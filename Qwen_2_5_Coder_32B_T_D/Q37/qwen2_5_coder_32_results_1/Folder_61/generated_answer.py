def filter_chars(s):
    chars_to_remove = {s[i] for i in range(5, 7) if 'G' <= s[i] <= 'p'}
    return ''.join((c for c in s if c not in chars_to_remove))