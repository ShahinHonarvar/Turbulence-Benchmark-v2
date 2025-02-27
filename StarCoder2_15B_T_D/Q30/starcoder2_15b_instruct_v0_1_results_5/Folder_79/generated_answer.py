def insert_before_character(input_string):
    output_string = ''
    for char in input_string:
        if char == 'E':
            output_string += 'EE'
        else:
            output_string += char
    return output_string