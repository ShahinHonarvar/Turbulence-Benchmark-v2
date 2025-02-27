def filter_chars(s):
    chars_to_remove = set()
    for i in range(48, 75):
        char = chr(i)
        if '6' < char < '_':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s