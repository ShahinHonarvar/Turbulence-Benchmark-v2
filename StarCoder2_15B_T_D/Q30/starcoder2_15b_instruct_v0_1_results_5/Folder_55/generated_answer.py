def insert_before_character(string):
    return ''.join([c if c != 'u' else 'U' for c in string])