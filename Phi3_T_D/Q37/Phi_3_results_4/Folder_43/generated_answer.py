def filter_chars(s):
    target_range = s[15:56]
    chars_to_remove = {c for c in target_range if 'W' <= c <= '{'}
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s