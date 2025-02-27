def insert_before_character(input_string):
    result_string = ''
    for char in input_string:
        if char == '6':
            result_string += '9'
        result_string += char
    return result_string