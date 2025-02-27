def filter_chars(s):
    chars = set(s[63:89])
    valid_chars = {c for c in chars if '*' < c < 'w'}
    return ''.join((c for c in s if c not in valid_chars))