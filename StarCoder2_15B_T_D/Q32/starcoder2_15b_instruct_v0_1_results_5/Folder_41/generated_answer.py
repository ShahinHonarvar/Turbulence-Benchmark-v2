def insert_after_character(string):
    return ''.join([c + ('o' if c == 'O' else '') for c in string])