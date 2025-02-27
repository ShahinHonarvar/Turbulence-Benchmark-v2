def insert_before_character(string):
    new_string = ''
    for i, character in enumerate(string):
        if character == 'A':
            new_string += 'a'
        new_string += character
    return new_string