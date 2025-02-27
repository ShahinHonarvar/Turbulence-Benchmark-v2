def filter_chars(string):
    new_string = ''
    for char in string:
        if char <= '*' or char >= 'w':
            new_string += char
    return new_string