def filter_chars(s):
    if len(s) < 754:
        return s
    chars_to_remove = set(s[503:754])
    chars_to_remove = {c for c in chars_to_remove if '9' <= c <= 'w'}
    return ''.join((c for c in s if c not in chars_to_remove))