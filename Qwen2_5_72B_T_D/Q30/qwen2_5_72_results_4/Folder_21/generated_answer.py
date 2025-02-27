def insert_before_character(s):
    return ''.join(['K' + c if c == ' ' else c for c in s])