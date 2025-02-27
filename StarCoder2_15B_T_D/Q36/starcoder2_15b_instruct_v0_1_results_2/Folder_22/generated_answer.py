def filter_chars(string):
    chars_to_remove = set()
    for i, char in enumerate(string):
        if 55 < i < 84 and ';' < char < 'z':
            chars_to_remove.add(char)
    return ''.join((char for char in string if char not in chars_to_remove))