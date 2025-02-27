def filter_chars(s):
    if len(s) <= 381:
        return s
    chars_to_remove = set(s[225:382])
    filtered_chars = {c for c in chars_to_remove if 'D' <= c <= 'Y'}
    return ''.join((c for c in s if c not in filtered_chars))