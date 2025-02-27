def filter_chars(s):
    target_chars = set('mno')
    return ''.join((c for c in s if c not in target_chars))