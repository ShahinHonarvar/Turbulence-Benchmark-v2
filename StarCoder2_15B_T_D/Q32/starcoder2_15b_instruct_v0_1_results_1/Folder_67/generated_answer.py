def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'j':
            output_string += '1'
    return output_string