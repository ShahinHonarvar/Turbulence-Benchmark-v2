def insert_after_character(input_string):
    output_string = ''
    for i, c in enumerate(input_string):
        output_string += c
        if c == 'A':
            output_string += 'H'
    return output_string