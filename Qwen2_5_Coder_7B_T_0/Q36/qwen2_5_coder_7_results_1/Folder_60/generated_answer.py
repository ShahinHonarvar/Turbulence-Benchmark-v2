def filter_chars(s):
    target_chars = set('ghij')
    return ''.join((c for c in s if c not in target_chars))