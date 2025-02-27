def insert_after_character(input_string):
    result_string = ''
    for char in input_string:
        result_string += char
        if char == 'a':
            result_string += 'A'
    return result_string