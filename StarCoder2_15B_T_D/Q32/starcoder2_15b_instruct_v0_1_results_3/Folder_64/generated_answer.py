def insert_after_character(string):
    return ''.join([c + ('u' if c == 'u' else '') for c in string])