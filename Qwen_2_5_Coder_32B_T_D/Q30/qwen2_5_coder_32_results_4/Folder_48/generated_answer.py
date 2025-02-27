def insert_before_character(s):
    return ''.join(('U' + c if c == 'S' else c for c in s))