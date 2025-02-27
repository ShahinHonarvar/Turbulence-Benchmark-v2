def filter_chars(s):
    chars_to_remove = [chr(c) for c in range(32, 84) if 'm' < chr(c) < 'w']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s