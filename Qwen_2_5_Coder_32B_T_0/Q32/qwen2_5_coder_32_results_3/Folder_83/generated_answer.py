def insert_after_character(s):
    return ''.join((c + 'e' if c == 'E' else c for c in s))