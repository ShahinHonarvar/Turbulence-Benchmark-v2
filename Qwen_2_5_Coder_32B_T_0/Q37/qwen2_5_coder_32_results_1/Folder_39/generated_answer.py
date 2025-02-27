def filter_chars(s):
    chars_to_remove = set(s[52:82]) & set('ABCDEFGHIJKLMNOPQRU')
    return ''.join((c for c in s if c not in chars_to_remove))