def insert_after_character(s):
    return ''.join((f'Mf{c}' if c == 'M' else c for c in s))