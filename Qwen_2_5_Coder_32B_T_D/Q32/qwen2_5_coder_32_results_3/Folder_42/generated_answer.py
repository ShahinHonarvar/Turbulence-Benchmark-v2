def insert_after_character(s):
    return ''.join((''.join((c, 'j')) if c == 'O' else c for c in s))