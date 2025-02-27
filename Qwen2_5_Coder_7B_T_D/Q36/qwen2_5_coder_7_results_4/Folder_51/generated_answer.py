def filter_chars(s):
    chars_to_remove = set()
    for i in range(58, 81):
        char = chr(i)
        if '5' < char < '>':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s