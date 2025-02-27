def filter_chars(s):
    chars_to_remove = set(s[32:47]) & set('0123456789abcdefghijk')
    return ''.join((c for c in s if c not in chars_to_remove))