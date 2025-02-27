def insert_before_character(s):
    return ''.join(('m' + c if c == 'F' else c for c in s))