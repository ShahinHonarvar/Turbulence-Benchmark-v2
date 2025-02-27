def filter_chars(s):
    chars_to_remove = {c for c in s[299:418] if '9' < c < 'P'}
    return ''.join((c for c in s if c not in chars_to_remove))