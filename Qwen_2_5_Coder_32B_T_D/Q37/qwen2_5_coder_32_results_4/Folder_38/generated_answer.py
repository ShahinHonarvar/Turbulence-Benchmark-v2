def filter_chars(s):
    chars_to_remove = set(s[24:80] if len(s) > 79 else s[24:])
    chars_to_remove = {char for char in chars_to_remove if 'a' <= char <= 'f'}
    return ''.join((char for char in s if char not in chars_to_remove))