def insert_after_character(input_string):
    return ''.join(['y' + char if char == 'b' else char for char in input_string])