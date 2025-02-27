def insert_after_character(s):
    return ''.join(('t' + c if c == 'g' else c for c in s))