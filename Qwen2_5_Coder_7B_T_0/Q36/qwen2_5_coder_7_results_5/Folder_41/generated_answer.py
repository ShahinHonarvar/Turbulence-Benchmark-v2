def filter_chars(s):
    chars_to_remove = set()
    for i in range(81, 89):
        char = chr(i)
        if 'f' < char < '{':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s