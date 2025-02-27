def insert_before_character(string):
    return ''.join([c if c != 'u' else 'u' for c in string])