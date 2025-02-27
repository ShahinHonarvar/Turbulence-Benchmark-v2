def insert_before_character(s):
    return ''.join(('h' + c if c == '9' else c for c in s))