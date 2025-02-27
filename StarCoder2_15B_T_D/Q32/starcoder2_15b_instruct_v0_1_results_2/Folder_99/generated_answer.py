def insert_after_character(string):
    return ''.join([c + ('W' if c == 'a' else '') for c in string])