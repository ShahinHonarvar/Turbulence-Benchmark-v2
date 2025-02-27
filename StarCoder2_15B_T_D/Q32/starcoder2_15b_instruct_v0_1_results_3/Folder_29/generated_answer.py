def insert_after_character(string):
    modified_string = ''
    for character in string:
        modified_string += character
        if character == 'N':
            modified_string += 'z'
    return modified_string