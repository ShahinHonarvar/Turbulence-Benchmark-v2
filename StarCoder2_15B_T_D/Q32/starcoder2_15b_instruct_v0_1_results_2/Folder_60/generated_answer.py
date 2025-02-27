def insert_after_character(string):
    return ''.join([c if c != 'C' else 'CP' for c in string])