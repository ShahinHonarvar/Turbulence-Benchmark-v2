def insert_after_character(s):
    return ''.join(('u' + c if c == 'U' else c for c in s))