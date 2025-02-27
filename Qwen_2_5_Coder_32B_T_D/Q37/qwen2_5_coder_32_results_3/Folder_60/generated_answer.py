def filter_chars(s):
    if len(s) <= 77:
        return s
    chars_to_remove = set(s[12:78])
    chars_to_remove = {char for char in chars_to_remove if ':' <= char <= 'L'}
    return ''.join((char for char in s if char not in chars_to_remove))