def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        output_string += character
        if character == '9':
            output_string += 'M'
    return output_string