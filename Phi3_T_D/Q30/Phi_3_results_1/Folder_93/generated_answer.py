def insert_before_character(s):
    return ''.join((f'4{c}' if c == 'Y' else c for c in s))