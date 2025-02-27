def insert_before_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'E':
            output_string += 'E'
    return output_string