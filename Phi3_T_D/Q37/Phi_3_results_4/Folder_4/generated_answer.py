def filter_chars(s):
    start, end = (19, 33)
    chars_to_remove = {c for c in s[start:end + 1] if 'S' <= c <= '{'}
    s = ''.join((c for c in s if c not in chars_to_remove))
    return s