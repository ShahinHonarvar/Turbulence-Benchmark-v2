def insert_before_character(string):
    return ''.join([c if c != 'e' else 'ec' for c in string])