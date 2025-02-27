def insert_after_character(input_string):
    modified_string = ''
    for char in input_string:
        if char == 'N':
            modified_string += 'Nz'
        else:
            modified_string += char
    return modified_string