def filter_chars(string):
    new_string = ''
    for char in string:
        if not (char > 'S' and char < 'm'):
            new_string += char
    return new_string