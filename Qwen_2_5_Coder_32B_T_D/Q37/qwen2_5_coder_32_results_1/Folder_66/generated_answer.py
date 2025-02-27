def filter_chars(s):
    if len(s) < 86:
        return s
    chars_to_remove = set(s[27:86])
    chars_to_remove = {char for char in chars_to_remove if 'c' <= char <= 'i'}
    return ''.join((char for char in s if char not in chars_to_remove))