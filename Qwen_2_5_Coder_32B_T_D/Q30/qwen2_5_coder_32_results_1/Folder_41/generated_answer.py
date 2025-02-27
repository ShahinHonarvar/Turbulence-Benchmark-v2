def insert_before_character(s):
    return ''.join(['o' + c if c == 'O' else c for c in s])