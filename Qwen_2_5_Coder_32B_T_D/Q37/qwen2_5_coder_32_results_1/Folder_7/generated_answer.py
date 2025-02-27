def filter_chars(s):
    if len(s) < 723:
        return s
    chars_to_remove = set(s[521:723])
    filtered_chars = {c for c in chars_to_remove if '>' <= c <= '_'}
    return ''.join((c for c in s if c not in filtered_chars))