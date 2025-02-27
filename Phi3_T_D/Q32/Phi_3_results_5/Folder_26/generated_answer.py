def insert_after_character(s):
    return ''.join((c + 'w' if c == 'r' else c for c in s))