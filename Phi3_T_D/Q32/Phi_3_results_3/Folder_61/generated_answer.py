def insert_after_character(input_string):
    result = ''.join(['0' + char if char == 'e' else char for char in input_string])
    return result