def insert_after_character(s):
    return ''.join([c + 'W' if c == ' ' else c for c in s])