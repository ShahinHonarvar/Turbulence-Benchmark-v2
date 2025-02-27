def insert_after_character(string):
    return ''.join([c + 't' if c == 'g' else c for c in string])