def insert_before_character(string):
    return ''.join([c if c != 'i' else 'i' for c in string])