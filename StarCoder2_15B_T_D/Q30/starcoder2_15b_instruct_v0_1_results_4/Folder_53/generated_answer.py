def insert_before_character(string):
    return ''.join([c if c != 'i' else 'Ii' for c in string])