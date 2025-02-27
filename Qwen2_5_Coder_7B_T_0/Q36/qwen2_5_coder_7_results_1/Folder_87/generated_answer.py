def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(33, 62) if chr(i) > '3' and chr(i) < 'D']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s