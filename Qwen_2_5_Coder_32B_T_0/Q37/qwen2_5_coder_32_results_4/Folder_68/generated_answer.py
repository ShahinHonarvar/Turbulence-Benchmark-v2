def filter_chars(s):
    chars_to_remove = set(s[7:10])
    chars_to_remove = {c for c in chars_to_remove if '6' <= c <= 'w'}
    return ''.join((c for c in s if c not in chars_to_remove))