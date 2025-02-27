def insert_after_character(input_string):
    result = ''
    previous_char = ''
    for char in input_string:
        if char == ' ' and previous_char == ' ':
            result += '  '
        else:
            result += char
        previous_char = char
    return result