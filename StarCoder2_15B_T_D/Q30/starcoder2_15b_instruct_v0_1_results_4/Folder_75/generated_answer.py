def insert_before_character(string):
    return ''.join([c if c != 'U' else 'qU' for c in string])