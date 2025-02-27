def insert_before_character(string):
    return ''.join([c if c != 'e' else '0e' for c in string])