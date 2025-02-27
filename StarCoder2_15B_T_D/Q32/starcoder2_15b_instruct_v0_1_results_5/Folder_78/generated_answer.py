def insert_after_character(string):
    return ''.join([c if c != 'H' else 'Hs' for c in string])