def filter_chars(s):
    to_remove = set([char for char in s[19:34] if 'S' <= char <= '{'])
    return ''.join([char for char in s if char not in to_remove])