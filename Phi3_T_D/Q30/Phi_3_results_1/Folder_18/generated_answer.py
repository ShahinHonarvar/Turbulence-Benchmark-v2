def insert_before_character(s):
    return ''.join(['l' + c if c == 'K' else c for c in s])