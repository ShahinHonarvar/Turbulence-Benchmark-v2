def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'O':
            output_string += 'O'
    return output_string