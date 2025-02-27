def insert_before_character(string):
    new_string = ''
    for character in string:
        if character == 'U':
            new_string += 'uU'
        else:
            new_string += character
    return new_string