def filter_chars(s):
    chars_to_remove = set([c for c in s[373:902] if 'T' <= c <= 'h'])
    return ''.join([c for c in s if c not in chars_to_remove])