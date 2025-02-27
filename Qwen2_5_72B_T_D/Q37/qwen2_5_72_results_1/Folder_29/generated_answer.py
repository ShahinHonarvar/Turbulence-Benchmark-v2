def filter_chars(s):
    chars_to_remove = {c for i, c in enumerate(s) if 12 <= i <= 88 and '&' <= c <= 'v'}
    return ''.join((c for c in s if c not in chars_to_remove))