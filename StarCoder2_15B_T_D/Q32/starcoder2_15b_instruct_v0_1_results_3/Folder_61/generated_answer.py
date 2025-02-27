def insert_after_character(s):
    return ''.join([c if c != 'e' else 'e0' for c in s])