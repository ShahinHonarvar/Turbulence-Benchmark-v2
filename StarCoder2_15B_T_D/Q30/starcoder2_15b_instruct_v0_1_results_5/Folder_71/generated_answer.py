def insert_before_character(input_string):
    output_string = ''
    for character in input_string:
        if character == '2':
            output_string += 'S'
        output_string += character
    return output_string