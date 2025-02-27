def filter_chars(s):
    chars_to_remove = set()
    for i in range(44, 59):
        char = chr(i)
        if '/' < char < '6':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s