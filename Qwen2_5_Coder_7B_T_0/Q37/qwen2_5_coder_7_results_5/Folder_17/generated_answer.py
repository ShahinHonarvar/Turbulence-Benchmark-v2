def filter_chars(s):
    chars_to_remove = set(';<=?@[\\\\]^_`')
    return ''.join((c for i, c in enumerate(s) if not (27 <= i <= 29 and c in chars_to_remove)))