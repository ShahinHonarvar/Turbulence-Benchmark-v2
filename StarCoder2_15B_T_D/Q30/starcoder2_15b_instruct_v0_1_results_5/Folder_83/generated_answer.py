def insert_before_character(string):
    return ''.join([char if char != 'E' else 'eE' for char in string])