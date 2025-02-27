def filter_chars(s):
    chars_to_remove = set(s[33:71] if len(s) > 70 else s[33:])
    chars_to_remove = {c for c in chars_to_remove if '7' <= c <= 'k'}
    return ''.join((c for c in s if c not in chars_to_remove))