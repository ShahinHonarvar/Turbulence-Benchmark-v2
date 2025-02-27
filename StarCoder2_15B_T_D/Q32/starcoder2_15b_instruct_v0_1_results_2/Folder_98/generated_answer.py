def insert_after_character(string):
    return ''.join([c if c != 'U' else 'uU' for c in string])