def filter_chars(s):
    chars_to_remove = set([char for char in s[19:34] if 'S' <= char <= '{'])
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result