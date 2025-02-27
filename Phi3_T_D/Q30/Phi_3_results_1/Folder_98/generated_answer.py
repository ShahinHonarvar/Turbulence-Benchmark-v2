def insert_before_character(input_string):
    return ''.join(['u' + c if c == 'U' else c for c in input_string])