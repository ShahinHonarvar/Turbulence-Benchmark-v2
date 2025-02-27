def filter_chars(s):
    target_chars = set('TUVWXYZ')
    return ''.join((char for char in s if char not in target_chars))