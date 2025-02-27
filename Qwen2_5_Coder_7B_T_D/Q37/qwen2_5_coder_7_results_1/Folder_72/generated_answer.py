def filter_chars(s):
    chars_to_remove = set('HJKLMNPQRSTUVWXYZ')
    return ''.join([char for char in s if (ord(char) < 35 or ord(char) > 51) or char not in chars_to_remove])