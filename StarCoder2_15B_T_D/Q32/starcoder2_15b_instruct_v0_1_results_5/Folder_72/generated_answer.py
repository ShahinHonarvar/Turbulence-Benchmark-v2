def insert_after_character(input_string):
    return ''.join([c if c != 'O' else 'Od' for c in input_string])