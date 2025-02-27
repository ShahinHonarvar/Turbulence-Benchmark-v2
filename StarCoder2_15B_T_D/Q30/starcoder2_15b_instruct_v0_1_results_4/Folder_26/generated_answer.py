def insert_before_character(string):
    return ''.join([c if c != 'r' else 'wr' for c in string])