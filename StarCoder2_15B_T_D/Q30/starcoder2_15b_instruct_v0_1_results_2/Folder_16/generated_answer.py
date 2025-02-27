def insert_before_character(string):
    new_string = ''
    for i, char in enumerate(string):
        if char == 'w':
            new_string += 'n'
        new_string += char
    return new_string