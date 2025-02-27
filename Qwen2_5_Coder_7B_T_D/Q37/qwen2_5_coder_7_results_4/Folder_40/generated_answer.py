def filter_chars(s):
    chars_to_remove = set('*abcdefghijklmnopqrstu')
    return ''.join((ch for ch in s if ch not in chars_to_remove))