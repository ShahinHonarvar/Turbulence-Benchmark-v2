def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(33, 85) if chr(i) > 'm' and chr(i) < 'w']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s