def filter_chars(s):
    chars_to_remove = set('VWXYZ')
    return ''.join([char for i, char in enumerate(s) if i < 51 or i > 77 or char not in chars_to_remove])