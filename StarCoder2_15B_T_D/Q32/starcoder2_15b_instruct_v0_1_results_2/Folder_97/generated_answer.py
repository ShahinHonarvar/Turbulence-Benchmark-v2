def insert_after_character(string):
    return ''.join([c if c != 'o' else 'oh' for c in string])