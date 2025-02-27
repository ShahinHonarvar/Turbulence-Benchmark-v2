def filter_chars(s):
    chars_to_remove = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ:;<=>?@\\\\]^_`{|}~')
    return ''.join((char for char in s if char not in chars_to_remove))