def insert_before_character(input_str):
    modified_str = input_str.replace(' ', ' X').replace('X ', ' X ')
    return modified_str.replace('X', ' ')