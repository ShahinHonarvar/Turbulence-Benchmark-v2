def insert_before_character(string):
    return ''.join([char if char != 'k' else 'k' + char for char in string])