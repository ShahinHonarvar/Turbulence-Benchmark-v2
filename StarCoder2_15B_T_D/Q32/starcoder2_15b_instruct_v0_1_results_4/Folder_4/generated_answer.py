def insert_after_character(string):
    new_string = ''
    for i, char in enumerate(string):
        new_string += char
        if char == 'a':
            new_string += '6'
    return new_string