def filter_chars(string):
    chars_to_remove = []
    for i, char in enumerate(string):
        if 27 <= i <= 29 and ';' <= char <= 'b':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string