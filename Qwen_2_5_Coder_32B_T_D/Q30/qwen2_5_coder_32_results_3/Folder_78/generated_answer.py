def insert_before_character(s):
    return ''.join(('s' + c if c == 'H' else c for c in s))