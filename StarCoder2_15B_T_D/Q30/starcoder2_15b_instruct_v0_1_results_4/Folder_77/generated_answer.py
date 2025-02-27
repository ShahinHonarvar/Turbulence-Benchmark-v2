def insert_before_character(string):
    return ''.join([char if char != '9' else 'h9' for char in string])