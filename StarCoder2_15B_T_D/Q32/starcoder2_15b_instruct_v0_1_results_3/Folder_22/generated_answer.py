def insert_after_character(string):
    return ''.join([c if c != 'U' else 'UU' for c in string])