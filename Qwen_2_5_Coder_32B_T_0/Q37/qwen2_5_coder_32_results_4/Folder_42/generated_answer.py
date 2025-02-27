def filter_chars(s):
    if len(s) < 75:
        return s
    chars_to_remove = set(s[73:75])
    chars_to_remove = {c for c in chars_to_remove if 'U' <= c <= 'l'}
    return ''.join((c for c in s if c not in chars_to_remove))