def filter_chars(s):
    chars_to_remove = set()
    for i in range(18, 64):
        char = chr(i)
        if '3' < char < 'B':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s