def insert_before_character(s):
    return ''.join(('A' + c if c == 'a' else c for c in s))