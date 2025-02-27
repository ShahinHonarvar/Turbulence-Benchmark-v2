def filter_chars(string):
    new_string = ''
    for char in string:
        if char <= 'M' or char >= '_':
            new_string += char
    return new_string