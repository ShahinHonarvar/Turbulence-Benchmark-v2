def filter_chars(s):
    if len(s) < 93:
        return s
    chars_to_remove = set(s[42:93]) & set(map(chr, range(ord('/'), ord('a') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))