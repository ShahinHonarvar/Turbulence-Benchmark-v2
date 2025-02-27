def filter_chars(s):
    t = s[82:93]
    chars_to_remove = {c for c in t if '!' < c < '*'}
    return ''.join((c for c in s if c not in chars_to_remove))