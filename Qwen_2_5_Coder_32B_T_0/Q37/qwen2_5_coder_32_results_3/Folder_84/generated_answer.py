def filter_chars(s):
    if len(s) < 921:
        return s
    chars_to_remove = set(s[138:921])
    chars_to_remove = {c for c in chars_to_remove if '6' <= c <= 'A'}
    return ''.join((c for c in s if c not in chars_to_remove))