def filter_chars(s):
    chars_to_remove = set(s[42:98] & set('*bcdefghijklmnop'))
    return ''.join((c for c in s if c not in chars_to_remove))