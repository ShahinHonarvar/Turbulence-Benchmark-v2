def insert_before_character(string):
    modified_string = ''
    for character in string:
        if character == 'E':
            modified_string += 'T'
        modified_string += character
    return modified_string