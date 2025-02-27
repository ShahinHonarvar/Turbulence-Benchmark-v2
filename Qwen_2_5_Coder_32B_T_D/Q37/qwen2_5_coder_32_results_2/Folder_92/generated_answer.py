def filter_chars(s):
    if len(s) < 5:
        return s
    chars_to_remove = set(s[4:5])
    chars_to_remove = {c for c in chars_to_remove if '7' <= c <= 'o'}
    return ''.join((c for c in s if c not in chars_to_remove))