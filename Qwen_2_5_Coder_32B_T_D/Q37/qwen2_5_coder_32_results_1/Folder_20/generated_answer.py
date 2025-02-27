def filter_chars(s):
    if len(s) < 98:
        return s
    chars_to_remove = set(s[25:98])
    chars_to_remove = {char for char in chars_to_remove if 'm' <= char <= 'w'}
    return ''.join((char for char in s if char not in chars_to_remove))