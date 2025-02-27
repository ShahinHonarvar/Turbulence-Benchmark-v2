def insert_after_character(string):
    new_string = ''
    for i, char in enumerate(string):
        new_string += char
        if char == 'r':
            new_string += '1'
    return new_string