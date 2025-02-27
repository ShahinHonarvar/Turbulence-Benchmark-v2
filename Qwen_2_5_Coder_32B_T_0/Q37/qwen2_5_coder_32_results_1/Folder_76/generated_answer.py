def filter_chars(s):
    if len(s) < 899:
        return s
    chars_to_remove = set(s[379:900])
    chars_to_remove = {c for c in chars_to_remove if 'M' <= c <= 'v'}
    return ''.join((c for c in s if c not in chars_to_remove))