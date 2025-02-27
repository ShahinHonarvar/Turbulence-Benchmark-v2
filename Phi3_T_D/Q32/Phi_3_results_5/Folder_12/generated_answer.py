def insert_after_character(s):
    return ''.join([' ' + c if c == 'I' else c for c in s])