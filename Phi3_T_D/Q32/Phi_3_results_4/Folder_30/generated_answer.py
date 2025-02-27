def insert_after_character(input_string):
    return ''.join(('F' + char if char == '4' else char for char in input_string))