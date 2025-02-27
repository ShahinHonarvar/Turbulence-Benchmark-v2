def insert_after_character(string):
    new_string = ''
    for index, character in enumerate(string):
        if character == 'a':
            new_string += 'an'
        else:
            new_string += character
    return new_string