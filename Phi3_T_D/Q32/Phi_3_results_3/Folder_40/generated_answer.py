def insert_after_character(input_string):
    updated_string = ''
    for char in input_string:
        updated_string += char
        if char == 'e':
            updated_string += 'e'
    return updated_string