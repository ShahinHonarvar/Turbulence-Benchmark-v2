def insert_before_character(string):
    modified_string = ''
    for character in string:
        if character == 'r':
            modified_string += '1'
        modified_string += character
    return modified_string