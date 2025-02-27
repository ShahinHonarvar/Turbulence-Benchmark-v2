def insert_before_character(s):
    return ''.join(['I' + c if c == 'Q' else c for c in s])