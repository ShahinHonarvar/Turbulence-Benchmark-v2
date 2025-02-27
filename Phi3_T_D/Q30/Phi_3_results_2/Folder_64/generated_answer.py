def insert_before_character(s):
    return ''.join(['u' + c if c == 'u' else c for c in s])