def filter_chars(s):
    chars_to_remove = set([char for char in s[25:98] if 'm' <= char <= 'w'])
    return ''.join([char for char in s if char not in chars_to_remove])