def insert_before_character(s):
    return ''.join(['W' + c if c == ' ' else c for c in s])