def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(64, 90) if chr(i) > '*' and chr(i) < 'w']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s