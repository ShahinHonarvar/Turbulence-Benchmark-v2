def insert_before_character(s):
    return ''.join(('9' + c if c == '6' else c for c in s))