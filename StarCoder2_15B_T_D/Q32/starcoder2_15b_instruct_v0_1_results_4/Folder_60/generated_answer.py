def insert_after_character(string):
    new_string = ''
    for character in string:
        new_string += character
        if character == 'C':
            new_string += 'P'
    return new_string