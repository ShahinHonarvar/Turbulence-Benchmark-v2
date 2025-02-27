def insert_before_character(s):
    return ''.join(('U' + c if c == 'u' else c for c in s))