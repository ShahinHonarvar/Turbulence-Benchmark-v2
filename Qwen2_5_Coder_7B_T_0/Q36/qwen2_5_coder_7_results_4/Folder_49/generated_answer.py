def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(47, 73) if chr(i) > 'D' and chr(i) < 'H']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s