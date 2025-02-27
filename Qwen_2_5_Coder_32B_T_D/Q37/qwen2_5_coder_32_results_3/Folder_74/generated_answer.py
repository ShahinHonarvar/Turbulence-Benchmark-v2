def filter_chars(s):
    t = s[19:33]
    chars_to_remove = {c for c in t if 'f' <= c <= 'o'}
    return ''.join((c for c in s if c not in chars_to_remove))