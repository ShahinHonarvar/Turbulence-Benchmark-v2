def filter_chars(s):
    chars_to_remove = {char for char in s[38:100] if 'A' <= char <= 'Q'}
    return ''.join((char for char in s if char not in chars_to_remove))