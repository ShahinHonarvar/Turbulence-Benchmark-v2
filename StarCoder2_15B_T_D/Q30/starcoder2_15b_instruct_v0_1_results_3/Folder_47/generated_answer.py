def insert_before_character(string):
    new_string = ''
    for character in string:
        if character == 'E':
            new_string += 'fE'
        else:
            new_string += character
    return new_string