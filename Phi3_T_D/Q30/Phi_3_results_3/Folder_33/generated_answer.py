def insert_before_character(s):
    return ''.join(['n' + c if c == 'a' else c for c in s])