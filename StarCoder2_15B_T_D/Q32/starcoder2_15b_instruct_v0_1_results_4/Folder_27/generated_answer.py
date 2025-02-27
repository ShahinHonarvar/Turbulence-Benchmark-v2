def insert_after_character(string):
    return ''.join([c if c != 'N' else 'Nj' for c in string])