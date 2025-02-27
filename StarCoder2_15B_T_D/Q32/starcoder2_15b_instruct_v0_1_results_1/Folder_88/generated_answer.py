def insert_after_character(input_string: str) -> str:
    output_string = ''
    for character in input_string:
        if character == 'a':
            output_string += 'at'
        else:
            output_string += character
    return output_string