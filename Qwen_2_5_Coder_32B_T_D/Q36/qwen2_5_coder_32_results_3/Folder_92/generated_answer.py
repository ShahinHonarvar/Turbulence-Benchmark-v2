def filter_chars(s):
    t = s[1:6]
    chars_to_remove = {c for c in t if ',' < c < 'f'}
    return ''.join((c for c in s if c not in chars_to_remove))