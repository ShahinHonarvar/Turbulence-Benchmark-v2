def filter_chars(s):
    chars_to_remove = set(s[69:81] if len(s) > 80 else s[69:])
    chars_to_remove = {char for char in chars_to_remove if '@' <= char <= 'p'}
    return ''.join((char for char in s if char not in chars_to_remove))