def insert_after_character(input_string):
    modified_string = ''
    for char in input_string:
        modified_string += char
        if char == 'U':
            modified_string += 'a'
    return modified_string