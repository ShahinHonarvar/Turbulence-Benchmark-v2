def insert_after_character(string):
    return ''.join([c if c != 'c' else 'Gc' for c in string])