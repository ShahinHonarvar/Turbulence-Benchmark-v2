def filter_chars(s):
    chars_to_remove = set(s[36:80])
    chars_to_remove = {c for c in chars_to_remove if '2' <= c <= 's'}
    return ''.join((c for c in s if c not in chars_to_remove))