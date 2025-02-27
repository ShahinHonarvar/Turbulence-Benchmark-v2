def insert_after_character(string):
    return ''.join([c + ('S' if c == '2' else '') for c in string])