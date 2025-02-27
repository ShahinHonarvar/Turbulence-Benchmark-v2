def insert_after_character(string):
    return ''.join([c if c != 'e' else 'Ee' for c in string])