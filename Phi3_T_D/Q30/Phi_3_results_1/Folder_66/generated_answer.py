def insert_before_character(s, ch='k'):
    return ''.join([c + 'k' if c == ch else c for c in s])