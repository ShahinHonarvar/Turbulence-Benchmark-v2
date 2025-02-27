def insert_after_character(input_string):
    new_string = ''
    for char in input_string:
        new_string += char + 'EE' if char == 'E' else char
    return new_string