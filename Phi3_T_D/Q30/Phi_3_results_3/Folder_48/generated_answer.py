def insert_before_character(input_string):
    modified_string = ''
    for char in input_string:
        if char == 'S':
            modified_string += 'US'
        else:
            modified_string += char
    return modified_string