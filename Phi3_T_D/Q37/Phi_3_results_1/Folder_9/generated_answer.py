def filter_chars(s):
    target_chars = set('ABCDEFGHIJKLMNOPQ')
    return ''.join((c for i, c in enumerate(s, start=1) if i < 38 or i > 99 or c not in target_chars))