def insert_before_character(input_string):
    return input_string.replace('u', 'Uu')[:-1] if 'u' in input_string else input_string