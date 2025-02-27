def insert_after_character(input_string):
    result_string = ''
    for char in input_string:
        result_string += char
        if char == 'o':
            result_string += 'a'
    return result_string