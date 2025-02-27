def insert_after_character(s):
    return ''.join((c + ('W' if c == 'e' else '') for c in s))