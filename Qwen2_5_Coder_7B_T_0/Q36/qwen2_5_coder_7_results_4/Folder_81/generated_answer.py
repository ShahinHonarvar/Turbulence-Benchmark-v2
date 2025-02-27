def filter_chars(s):
    chars_to_remove = set()
    for i in range(51, 76):
        char = chr(i)
        if '5' < char < 'f':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s