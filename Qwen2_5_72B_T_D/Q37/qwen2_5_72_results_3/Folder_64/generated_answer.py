def filter_chars(s):
    chars_to_remove = {char for char in s[1:8] if 'L' <= char <= 'a'}
    return ''.join((char for char in s if char not in chars_to_remove))