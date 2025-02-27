def insert_before_character(input_string):
    modified_string = ''
    for char in input_string:
        modified_string += 't' if char == 'g' else char
    return modified_string