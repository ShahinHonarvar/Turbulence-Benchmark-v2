def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'F':
            new_string += 'm'
        new_string += char
    return new_string