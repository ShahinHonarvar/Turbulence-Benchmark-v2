def filter_chars(s):
    chars_to_remove = set(s[13:29] if len(s) > 28 else s[13:])
    chars_to_remove = {char for char in chars_to_remove if 'c' <= char <= 'n'}
    return ''.join((char for char in s if char not in chars_to_remove))