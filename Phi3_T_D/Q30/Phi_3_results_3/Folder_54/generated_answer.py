def insert_before_character(s):
    return ''.join(['f' + c if c == 'M' else c for c in s])