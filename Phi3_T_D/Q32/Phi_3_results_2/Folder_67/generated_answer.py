def insert_after_character(s):
    return ''.join(('1' + c if c == 'j' else c for c in s))