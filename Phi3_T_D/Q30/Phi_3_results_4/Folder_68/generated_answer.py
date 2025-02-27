def insert_before_character(s):
    return ''.join(['0' + c if c == 'i' else c for c in s])