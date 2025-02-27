def insert_before_character(input_string):
    output_string = ''
    for char in input_string:
        if char == 'T':
            output_string += 'V'
        output_string += char
    return output_string