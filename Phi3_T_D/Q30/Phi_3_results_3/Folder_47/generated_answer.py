def insert_before_character(input_string):
    result = ''
    for char in input_string:
        result += 'f' if char == 'E' else char
    return result