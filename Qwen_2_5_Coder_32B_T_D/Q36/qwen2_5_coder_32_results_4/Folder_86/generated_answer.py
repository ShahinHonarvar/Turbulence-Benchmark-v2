def filter_chars(s):
    target_chars = set(s[672:709])
    remove_chars = {c for c in target_chars if 'X' < c < '}'}
    return ''.join((c for c in s if c not in remove_chars))