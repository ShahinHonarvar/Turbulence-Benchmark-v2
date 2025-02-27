def insert_after_character(string: str) -> str:
    output_string = ''
    for character in string:
        output_string += character
        if character == 'w':
            output_string += 'n'
    return output_string