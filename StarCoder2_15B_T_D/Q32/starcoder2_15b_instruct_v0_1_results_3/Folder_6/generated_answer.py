def insert_after_character(string):
    return ''.join([char + ('u' if char == 'X' else '') for char in string])