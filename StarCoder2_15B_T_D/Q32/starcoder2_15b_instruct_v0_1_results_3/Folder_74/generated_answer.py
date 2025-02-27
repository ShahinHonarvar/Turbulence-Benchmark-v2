def insert_after_character(string):
    return ''.join([char if char != 'T' else ' T' for char in string])