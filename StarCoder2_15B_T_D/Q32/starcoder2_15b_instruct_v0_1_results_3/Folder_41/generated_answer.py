def insert_after_character(string):
    return ''.join([c if c != 'O' else 'Oo' for c in string])