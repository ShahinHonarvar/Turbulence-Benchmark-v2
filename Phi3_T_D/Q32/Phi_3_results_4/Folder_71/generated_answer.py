def insert_after_character(input_string):
    return ''.join(['S' + char if char == '2' else char for char in input_string])