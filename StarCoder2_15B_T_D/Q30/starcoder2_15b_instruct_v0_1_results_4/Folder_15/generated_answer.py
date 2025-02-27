def insert_before_character(string):
    return ''.join([c if c != 'o' else 'oo' for c in string])