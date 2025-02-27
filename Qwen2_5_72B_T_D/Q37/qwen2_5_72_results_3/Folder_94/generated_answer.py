def filter_chars(s):
    to_remove = set([char for char in s[51:97] if 'X' <= char <= 'p'])
    return ''.join([char for char in s if char not in to_remove])