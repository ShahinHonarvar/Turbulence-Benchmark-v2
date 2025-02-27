def insert_before_character(string):
    return ''.join([char if char != 'a' else 'ta' for char in string])