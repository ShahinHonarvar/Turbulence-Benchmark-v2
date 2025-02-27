def insert_after_character(input_string):
    result_string = ''
    for char in input_string:
        result_string += char
        if char == 'I':
            result_string += 'i'
    return result_string