def insert_before_character(s):
    return ''.join(('a' + c if c == 'A' else c for c in s))