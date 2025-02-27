def filter_chars(s):
    remove_chars = {c for c in s[21:25] if '5' < c < '}'}
    return ''.join((c for c in s if c not in remove_chars))