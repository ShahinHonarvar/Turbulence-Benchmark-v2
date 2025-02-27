def insert_before_character(s):
    return ''.join(['Q' + c if c == 'm' else c for c in s])