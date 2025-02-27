def filter_chars(s):
    chars = set(s[35:41])
    chars_to_filter = {char for char in chars if ')' <= char <= 'l'}
    return ''.join((char for char in s if char not in chars_to_filter))