def insert_before_character(s):
    return ''.join([' ' + c if c == 'T' else c for c in s])