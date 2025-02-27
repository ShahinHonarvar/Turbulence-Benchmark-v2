def insert_after_character(input_string):
    output_string = ''
    for index, character in enumerate(input_string):
        output_string += character
        if character == 'c':
            output_string += 'G'
    return output_string