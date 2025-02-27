def insert_after_character(string):
    new_string = ''
    for index, character in enumerate(string):
        new_string += character
        if character == 'g':
            new_string += 't'
    return new_string