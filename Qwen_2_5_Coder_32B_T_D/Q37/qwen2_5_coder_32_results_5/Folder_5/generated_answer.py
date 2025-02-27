def filter_chars(s):
    chars_to_remove = set(s[24:83]) & set('56789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`{|}~')
    return ''.join((c for c in s if c not in chars_to_remove))