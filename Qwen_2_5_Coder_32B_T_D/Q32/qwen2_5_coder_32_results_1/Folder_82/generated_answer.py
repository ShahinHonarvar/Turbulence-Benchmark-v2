def insert_after_character(s):
    return ''.join((c + ('I' if c == 'I' else '') for c in s))