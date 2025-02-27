def insert_before_character(input_string: str) -> str:
    output_string = ''
    for char in input_string:
        if char == '5':
            output_string += 'h'
        output_string += char
    return output_string