def insert_before_character(string):
    return ''.join([c if c != 'a' else 'a' for c in string])