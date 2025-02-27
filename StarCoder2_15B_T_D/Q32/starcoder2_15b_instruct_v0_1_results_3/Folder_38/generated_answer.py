def insert_after_character(string):
    new_string = ''
    for i, char in enumerate(string):
        if char == 'X':
            new_string += '6'
        new_string += char
    return new_string