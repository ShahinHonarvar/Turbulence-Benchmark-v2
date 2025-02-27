def insert_after_character(string):
    return ''.join([char + ('9' if char == '6' else '') for char in string])