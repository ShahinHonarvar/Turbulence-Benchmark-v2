def insert_after_character(string):
    return ''.join([c + ('E' if c == 'E' else '') for c in string])