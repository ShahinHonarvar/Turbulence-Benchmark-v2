def insert_before_character(s):
    return ''.join(['V' + c if c == 'R' else c for c in s])