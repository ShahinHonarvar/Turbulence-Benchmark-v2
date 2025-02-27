def filter_chars(s):
    t = s[61:71]
    chars_to_remove = {c for c in t if '0' <= c <= '@'}
    return ''.join((c for c in s if c not in chars_to_remove))