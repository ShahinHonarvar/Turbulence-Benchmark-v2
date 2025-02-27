def insert_after_character(input_string):
    modified_string = ''
    for char in input_string:
        modified_string += char
        if char == 'B':
            modified_string += 'N'
    return modified_string