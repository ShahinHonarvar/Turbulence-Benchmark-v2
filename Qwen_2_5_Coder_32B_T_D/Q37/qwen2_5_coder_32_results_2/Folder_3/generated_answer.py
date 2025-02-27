def filter_chars(s):
    t = s[37:57]
    chars_to_remove = {c for c in t if '6' <= c <= '_'}
    return ''.join((c for c in s if c not in chars_to_remove))