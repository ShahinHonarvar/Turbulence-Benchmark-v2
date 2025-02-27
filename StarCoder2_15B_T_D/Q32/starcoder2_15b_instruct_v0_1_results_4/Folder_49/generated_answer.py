def insert_after_character(string):
    return ''.join([c if c != 'i' else 'ii' for c in string])