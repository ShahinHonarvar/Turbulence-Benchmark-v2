def insert_before_character(string):
    return ''.join([c if c != 'j' else 'qj' for c in string])