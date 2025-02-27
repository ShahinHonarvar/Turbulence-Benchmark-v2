def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'e':
            output_string += 'W'
    return output_string