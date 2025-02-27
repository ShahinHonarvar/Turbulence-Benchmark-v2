def insert_before_character(string):
    return ''.join([c if c != 's' else 'ws' for c in string])