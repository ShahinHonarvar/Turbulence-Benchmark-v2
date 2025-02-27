def insert_before_character(input_string):
    result = ''
    for char in input_string:
        result += 'T' if char == 'U' else char
    return result