def insert_after_character(string):
    return ''.join([c if c != 'o' else 'ao' for c in string])