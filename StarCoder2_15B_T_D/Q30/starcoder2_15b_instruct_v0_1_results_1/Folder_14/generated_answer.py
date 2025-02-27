def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == ' ':
            new_string += ' '
        new_string += char
    return new_string