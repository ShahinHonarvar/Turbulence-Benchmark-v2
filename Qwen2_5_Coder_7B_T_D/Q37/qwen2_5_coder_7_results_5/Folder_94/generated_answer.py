def filter_chars(s):
    chars_to_remove = set('XyZabcdeEfghijklmnp')
    return ''.join((ch for ch in s if ch not in chars_to_remove))