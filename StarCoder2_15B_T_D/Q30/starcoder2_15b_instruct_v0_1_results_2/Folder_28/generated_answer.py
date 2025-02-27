def insert_before_character(input_string):
    output_string = ''
    for i, c in enumerate(input_string):
        if c == 'r':
            output_string += '1r'
        else:
            output_string += c
    return output_string