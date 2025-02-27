def filter_chars(s):
    chars_to_remove = set(s[33:71]) & set('789:;<=>?@ABCDEFGHK')
    return ''.join((c for c in s if c not in chars_to_remove))