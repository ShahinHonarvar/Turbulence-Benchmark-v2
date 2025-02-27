def insert_before_character(s):
    return ''.join(('EE' if c == 'E' else c for c in s))